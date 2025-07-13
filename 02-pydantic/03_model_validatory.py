#step 1: Define the schema
from pydantic import BaseModel,EmailStr,AnyUrl,Field, field_validator, model_validator
from typing import List,Dict, Optional, Annotated

class Patient(BaseModel):
    name: str
    email: EmailStr
    age: int
    weight: float
    married: bool
    allergies: list[str]
    contact_info: dict[str,str]

    @model_validator(mode='after')
    def validate_emergency_contact(cls,model):
        if model.age > 60 and 'emergency' not in model.contact_info:
            raise ValueError("Emergency contact is required for patients above 60")
        return model
  
def update_patient_data(patient:Patient):
    print(f"Patient name: {patient.name}, Patient email: {patient.email}, Patient age: {patient.age},  Patient weight: {patient.weight}, \
    Patient married: {patient.married}, Patient allergies: {patient.allergies}, Patient contact info: {patient.contact_info}")
    print("updated into database successfully")

patient_info = {'name':'John','email':'john@hdfgmailc.com','age':61,'weight':70.5,'married':True,\
                'allergies':['pollen','dust'],'contact_info':{'phone':'1234567890', 'emergency':'1234567890'}}

patient = Patient(**patient_info)
update_patient_data(patient)
