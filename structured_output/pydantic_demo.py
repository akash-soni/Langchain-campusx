from pydantic import BaseModel, EmailStr, Field
from typing import Optional

# class Student(BaseModel):
#     name: str


# new_student = {'name':'akash'}

# Student = Student(**new_student)

# print(Student)


# fixing default values
class Student(BaseModel):
    name: str = 'akash'
    age: Optional[int] = None
    #email: EmailStr
    cgpa: float = Field(gt=0,lt=20, default=5, description='A decimal value representing the cgpa of the student')

##new_student = {'age': 32, 'email': 'akash.soni@gmail.com', 'cgpa':15}
new_student = {'age': 32,'cgpa':15}
Student = Student(**new_student)

print(Student)

student_dict = dict(Student)

print(student_dict['age'])

student_json = Student.model_dump_json()