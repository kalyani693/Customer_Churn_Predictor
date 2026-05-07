from sqlalchemy import Column,VARCHAR,Float,Integer
from database_relational.db_main import base

#--table1    
class user_data(base):
    __tablename__="user_data"
    
    id=Column(Integer,primary_key=True)
    family =Column(VARCHAR(50),nullable=False)
    SeniorCitizen=Column(VARCHAR(50),nullable=False)
    tenure=Column(Float,nullable=False)
    InternetService=Column(VARCHAR(50),nullable=False)
    OnlineSecurity=Column(VARCHAR(50),nullable=False)
    OnlineBackup=Column(VARCHAR(50),nullable=False)
    DeviceProtection=Column(VARCHAR(50),nullable=False)
    TechSupport=Column(VARCHAR(50),nullable=False)
    Streaming=Column(VARCHAR(50),nullable=False)
    Contract=Column(VARCHAR(50),nullable=False)
    PaperlessBilling=Column(VARCHAR(50),nullable=False)
    PaymentMethod=Column(VARCHAR(50),nullable=False)
    MonthlyCharges=Column(Float,nullable=False)
    TotalCharges=Column(Float,nullable=False)
    will_churn=Column(VARCHAR(50),nullable=False)


