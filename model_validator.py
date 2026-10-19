from pydantic import BaseModel , EmailStr , AnyUrl , Field , field_validator , model_validator
from typing import List , Dict , Optional , Annotated

class Patient(BaseModel):

    name: str
    email: EmailStr
    age: int
    weight: float
    married: Optional[bool] = None
    allergies: List[str]
    contact_details: Dict[str , str]

    @model_validator(mode = 'after')

    def validate_emergency_contact(cls , model):
        if model.age > 60 and 'emergency' not in model.contact_details:
            raise ValueError('Patients older than 60 must have an emergency contact')
        return model


def insert_patient_data(patient : Patient):
    print(patient.name)
    print(patient.age)
    print(patient.weight)
    print(patient.married)
    print(patient.allergies)
    print(patient.contact_details)
    print("Successfully Inserted Bhai!!!")


def update_patient_data(patient : Patient):
    print(patient.name)
    print(patient.age)
    print(patient.weight)
    print(patient.married)
    print(patient.allergies)
    print(patient.contact_details)
    print("Successfully Updated Bhai!!!")


patient_info = {'name' : 'Nischay' , 'email': 'nischay@icici.com'  , 'age' : '70' , 'weight' : 75.58 ,'allergies' : ['Pollen' , 'Dust' , 'Eggs'] , 'contact_details' : {'Phone' : '9876543210' , 'emergency' : '9874563210'}}

patient_1 = Patient(**patient_info) # Validation is performed here -> type coersion 

insert_patient_data(patient_1)