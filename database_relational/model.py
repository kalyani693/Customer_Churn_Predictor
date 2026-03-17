from sqlalchemy import Column,String ,Float,Integer
from database_relational.db_main import base

#--table1    
class user_data(base):
    __tablename__="user_data"
    
    id=Column(Integer,primary_key=True)
    Family =Column(String,nullable=False)
    SeniorCitizen=Column(String,nullable=False)
    tenure=Column(Float,nullable=False)
    InternetService=Column(String,nullable=False)
    OnlineSecurity=Column(String,nullable=False)
    OnlineBackup=Column(String,nullable=False)
    DeviceProtection=Column(String,nullable=False)
    TechSupport=Column(String,nullable=False)
    Streaming=Column(String,nullable=False)
    Contract=Column(String,nullable=False)
    PaperlessBilling=Column(String,nullable=False)
    PaymentMethod=Column(String,nullable=False)
    MonthlyCharges=Column(Float,nullable=False)
    TotalCharges=Column(Float,nullable=False)
    will_churn=Column(String,nullable=False)


