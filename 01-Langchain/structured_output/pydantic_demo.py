from pydantic import BaseModel, EmailStr, Field
from typing import Optional

# class Student(BaseModel):
#     name: str

#This is valid
# new_student = {'name':'akash'}

#This will not be accepted as the type hint is str and we are passing int
# new_student = {'name':123}

# Student = Student(**new_student)

# print(Student)


# fixing default values
class Student(BaseModel):
    #Default Validation: name is defaulted to 'akash'
    name: str = 'akash'
    
    #Optional Validation: age is optional and can be None
    age: Optional[int] = None

    #Builtin Validation:
    email: EmailStr

    # Field Validation:
    cgpa: float = Field(gt=0,lt=20, default=5, description='A decimal value representing the cgpa of the student')

##new_student = {'age': 32, 'email': 'akash.soni@gmail.com', 'cgpa':15}
new_student = {'age': 32,'cgpa':15}
Student = Student(**new_student)

print(Student)

student_dict = dict(Student)

print(student_dict['age'])

student_json = Student.model_dump_json()