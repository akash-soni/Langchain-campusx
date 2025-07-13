#step 1: Define the schema
from pydantic import BaseModel,EmailStr,AnyUrl,Field, field_validator, computed_field
from typing import List,Dict, Optional, Annotated

class Patient(BaseModel):
    name: str
    email: EmailStr
    age: int
    height: float
    weight: float
    married: bool
    allergies: list[str]
    contact_info: dict[str,str]

    @computed_field
    @property
    def bmi(self)->float:
        bmi = round(self.weight / (self.height ** 2),2)
        return bmi

def update_patient_data(patient:Patient):
    print(f"Patient name: {patient.name}, Patient email: {patient.email}, Patient age: {patient.age},patient height: {patient.height},  Patient weight: {patient.weight}, \
    Patient married: {patient.married}, Patient allergies: {patient.allergies}, Patient contact info: {patient.contact_info}, Patient bmi: {patient.bmi}")
 
patient_info = {'name':'John','email':'john@gmail.com','age':61,'height':170,'weight':70.5,'married':True,\
                'allergies':['pollen','dust'],'contact_info':{'phone':'1234567890'}}

patient = Patient(**patient_info)
update_patient_data(patient)
