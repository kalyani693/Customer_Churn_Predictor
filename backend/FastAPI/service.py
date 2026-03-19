#logic required for main file
from pydantic import BaseModel,Field
from typing import Annotated,Literal

class ChurnInput(BaseModel):
    SeniorCitizen:Annotated[Literal["Yes","No"],Field(default="Yes",description="Is user connected with this company?")]
    family:Annotated[Literal["Yes","No"],Field(...,description="Is user connected with family?")]
    tenure:Annotated[int,Field(...,gt=0,description="No of months user is connected")]
    InternetService:Annotated[Literal["DSL", "Fiber optic", "No"],Field(...,)]
    OnlineSecurity:Annotated[Literal["Yes","No","No internate"],Field(...,)]
    OnlineBackup:Annotated[Literal["Yes","No","No internate"],Field(...,)]
    DeviceProtection:Annotated[Literal["Yes","No","No internate"],Field(...,)]
    TechSupport:Annotated[Literal["Yes","No","No internate"],Field(...,)]
    Contract:Annotated[Literal["month to month", "one year", "two year"],Field(...,)]
    PaperlessBilling:Annotated[Literal["Yes","No"],Field(...,)]
    PaymentMethod:Annotated[Literal["Electronic check", "Mailed check", 
                                  "Bank transfer (automatic)", "Credit card (automatic)"],Field(...,)]
    Streaming:Annotated[Literal["Yes","No"],Field(...,)]
    MonthlyCharges:Annotated[float,Field(...,gt=0)]
    TotalCharges:Annotated[float,Field(...,gt=0)]

