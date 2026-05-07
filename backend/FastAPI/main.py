from fastapi import FastAPI,HTTPException,Depends,Query,Path,responses,status
from typing import List,Annotated
from database_relational import model
from FastAPI.service import ChurnInput
from database_relational.db_main import engine, sessionlocal
from sqlalchemy.orm import session
from database_relational.auth import get_db
from fastapi.middleware.cors import CORSMiddleware
from database_relational.auth import get_db 
from database_relational.model import user_data
from sqlalchemy import text
import pandas as pd
import numpy as np
from ml.load_models import model_features,predict_prob,model_version



app=FastAPI(title="Churn Predictor api")
#app.include_router(auth.router)
model.base.metadata.create_all(bind=engine)#creates tables

#middleware for cors
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

#dependencies
dependency=Annotated[session,Depends(get_db)]  #dependency 


#read_data
def get_data():
   db=sessionlocal()
   query=text("select * from user_data")
   result=db.execute(query)
   data=result.fetchall()
   data=[dict(row._mapping) for row in data]
   db.close()
   return data
        
@app.get("/",response_model=dict,status_code=status.HTTP_200_OK)
def home():
    return {"message":"Wellcome"}    

@app.get("/health",response_model=dict,status_code=status.HTTP_200_OK)
def health_check():
   return responses.JSONResponse(status_code=200,content={
      'Status':'ok',
      'Model version':model_version
   })

@app.get("/get_data",response_model=dict,status_code=status.HTTP_200_OK)
def read_data():
   data=get_data()
   return {'data':data}

@app.post("/predict",response_model=dict,status_code=status.HTTP_200_OK)#put dependency here
def predict(user_ip:ChurnInput, db:dependency):
   if user_ip: 
    df=pd.DataFrame(user_ip.model_dump(),index=[0])
    encoded_df=pd.get_dummies(df)
    encoded_df=pd.DataFrame(encoded_df).reindex(columns=model_features)#imp step
    #prediction result
    probability,y_Pred,prob=predict_prob(encoded_df)
    
        #3. Return proper response
   return {
            "will churn":y_Pred,
            "Probability of Churn":f"{probability}-({np.around(prob[1],2)})"}

@app.post("/save_data",response_model=dict,status_code=status.HTTP_200_OK)
def save_data(user_ip:ChurnInput, db:dependency):
    if user_ip:
        try:
            result=predict(user_ip,db)
            y_pred=result["will churn"]
            db_users=model.user_data(**user_ip.model_dump(),will_churn=y_pred)
            db.add(db_users)
            db.commit()
        except Exception as e:
            raise HTTPException(status_code=400,detail=f"error={e}")
    return {"Message": "Customer data saved successfully"}