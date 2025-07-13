#step 1: Define the schema
from pydantic import BaseModel,EmailStr,AnyUrl,Field, field_validator
from typing import List,Dict, Optional, Annotated

class Patient(BaseModel):
    name: str
    email: EmailStr
    age: int
    weight: float
    married: bool
    allergies: list[str]
    contact_info: dict[str,str]

    # Field validator method to validate the email domain
    # This method is class method
    @field_validator("email", mode='after')
    @classmethod
    def email_validator(cls,value):
        valid_domains = ["hdfc.com","icici.com"]
        domain_name = value.split("@")[1]
        if domain_name not in valid_domains:
            raise ValueError("Invalid email domain")
        return value
    
    # Field validator method to transform the name to uppercase
    @field_validator("name", mode='after')
    @classmethod
    def name_validator(cls,value):
        return value.upper()
    
    @field_validator("age", mode='after')
    @classmethod
    def age_validator(cls,value):
        if 5 < value < 65:
            return value
        else:
            raise ValueError("Age must be between 5 and 65")
    

def update_patient_data(patient:Patient):
    print(f"Patient name: {patient.name}, Patient email: {patient.email}, Patient age: {patient.age},  Patient weight: {patient.weight}, \
    Patient married: {patient.married}, Patient allergies: {patient.allergies}, Patient contact info: {patient.contact_info}")
    print("updated into database successfully")

patient_info = {'name':'John','email':'john@hdfc.com','age':'30','weight':70.5,'married':True,\
                'allergies':['pollen','dust'],'contact_info':{'phone':'1234567890'}}

patient = Patient(**patient_info) #validation -> type coersion
update_patient_data(patient)
