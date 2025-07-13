#step 1: Define the schema
from pydantic import BaseModel,EmailStr,AnyUrl,Field
from typing import List,Dict, Optional, Annotated

class Patient(BaseModel):
    NAME: Annotated[str,Field(min_length=3,max_length=50, title="Patient Name", description="The name of the patient should be between 3 and 50 characters", \
         examples=["JohnDoe","Jane Smith"])]
    age: int = Field(gt=5,lt=65)
    email: EmailStr
    linkedin_url: AnyUrl
    weight: Annotated[float,Field(gt=0,description="The weight of the patient should be greater than 0",strict=True)]
    married: Annotated[Optional[bool],Field(default=False, description="Whether the patient is married or not")]
    allergies: Annotated[Optional[list[str]],Field(min_items=1,max_items=5)]
    contact_info: dict[str,str]

def insert_patient_data(patient:Patient):
    print(f"Patient name: {patient.NAME}, Patient age: {patient.age}, Patient email: {patient.email}, Patient linkedin_url: {patient.linkedin_url}, Patient weight: {patient.weight},\
     Patient married: {patient.married}, Patient allergies: {patient.allergies}, Patient contact info: {patient.contact_info}")
    print("inserted into database successfully")

def update_patient_data(patient:Patient):
    print(f"Patient name: {patient.NAME}, Patient age: {patient.age}, Patient email: {patient.email}, Patient linkedin_url: {patient.linkedin_url}, Patient weight: {patient.weight}, \
    Patient married: {patient.married}, Patient allergies: {patient.allergies}, Patient contact info: {patient.contact_info}")
    print("updated into database successfully")

#STEP2: Define the data
PATIENT_INFO = {'NAME':'John','age':60,'email':'john@example.com','linkedin_url':'https://www.linkedin.com/in/john-doe/','weight':70.5,\
    'allergies':['pollen','dust'],'contact_info':{'phone':'1234567890'}}

PATIENT1 = Patient(**PATIENT_INFO)

#STEP3: Call the function
insert_patient_data(PATIENT1)
update_patient_data(PATIENT1)




