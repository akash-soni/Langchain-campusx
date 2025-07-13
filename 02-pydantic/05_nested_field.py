#step 1: Define the schema
from pydantic import BaseModel
from typing import List,Dict, Optional, Annotated

class Address(BaseModel):
    street: str
    city: str
    state: str
    zip: str

class Patient(BaseModel):
    name: str
    gender: str
    age: int
    address: Address


address_dict = {'street':'123 Main St','city':'Anytown','state':'CA','zip':'12345'}
address1 = Address(**address_dict)

patient_info = {'name':'John', 'gender':'male','age':61,'address':address1}

patient = Patient(**patient_info)

print(patient)
print(patient.address)
print(patient.address.street)
print(patient.address.city)
print(patient.address.state)
print(patient.address.zip)

