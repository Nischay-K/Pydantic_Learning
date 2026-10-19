from pydantic import BaseModel , EmailStr , AnyUrl , Field , field_validator , model_validator , computed_field
from typing import List , Dict , Optional , Annotated

class Patient(BaseModel):

    name: str
    email: EmailStr
    age: int
    weight: float #Kg
    height: float #Meter
    married: Optional[bool] = None
    allergies: List[str]
    contact_details: Dict[str , str]

    @computed_field()
    @property

    def calculate_bmi(self) -> float:

        bmi = round(self.weight/(self.height**2) , 2)
        return bmi

def insert_patient_data(patient : Patient):
    print(patient.name)
    print(patient.age)
    print(patient.weight)
    print(patient.height)
    print(patient.married)
    print(patient.allergies)
    print(patient.contact_details)
    print("BMI : ", patient.calculate_bmi)
    print("Successfully Inserted Bhai!!!")


def update_patient_data(patient : Patient):
    print(patient.name)
    print(patient.age)
    print(patient.weight)
    print(patient.height)
    print(patient.married)
    print(patient.allergies)
    print(patient.contact_details)
    print("BMI : ", patient.bmi)
    print("Successfully Updated Bhai!!!")


patient_info = {'name' : 'Nischay' , 'email': 'nischay@icici.com'  , 'age' : '70' , 'weight' : 75.58 , 'height' : 1.82 ,'allergies' : ['Pollen' , 'Dust' , 'Eggs'] , 'contact_details' : {'Phone' : '9876543210' , 'emergency' : '9874563210'}}

patient_1 = Patient(**patient_info) # Validation is performed here -> type coersion 

insert_patient_data(patient_1)