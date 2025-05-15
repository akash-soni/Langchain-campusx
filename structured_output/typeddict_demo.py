from typing import TypedDict

class Person(TypedDict):

    name: str
    age: int

# this is valid as per the type hint
new_person: Person = {'name':'akash','age':34}

# this is accepted but not valid as per the type hint
new_person1: Person = {'name':'akash','age':'34'} 

print(new_person)
print(new_person1)
