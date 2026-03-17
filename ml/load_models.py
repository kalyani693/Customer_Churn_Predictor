import pickle
import joblib

model_version='1.0'
try:
 model1=joblib.load("ml/model.pkl")
 model_features=joblib.load("ml/model_feature.pkl")

 print("model loaded successfully✔")
except Exception as e:
  print(e)

def predict_prob(encoded_df):
 prediction = model1.predict(encoded_df)[0]
 prob=(model1.predict_proba(encoded_df))[0]#returns prob of class 0 and class 1
 pred=(prob[1]>0.50).astype(int)
 if pred ==1:
       y_Pred="Yes"
 else:
       y_Pred="No" 

 if (0.0<prob[1]<=0.3):
       probability="Low"
 elif (0.3<prob[1]<=0.7):
       probability="Medium"
 else:
       probability="High" 

 return probability,y_Pred,prob               
