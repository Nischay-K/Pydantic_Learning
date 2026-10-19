from pydantic import BaseModel , EmailStr , AnyUrl , Field , field_validator
from typing import List , Dict , Optional , Annotated

class Patient(BaseModel):

    name: str
    email: EmailStr
    age: int
    weight: float
    married: Optional[bool] = None
    allergies: List[str]
    contact_details: Dict[str , str]

    #decorators is used for the email_validation case

    @field_validator('email')
    @classmethod

    def email_validator(cls , value):

        valid_domains = ['hdfs.com' , 'icici.com']
        #abc@gmail.com
        domain_name = value.split('@')[-1]

        if domain_name not in valid_domains:
            raise ValueError('Not a valid email domain!!')

        return value


    @field_validator('name') #field_validator works on two modes i.e mode = 'after'(Default) / 'before' they are totally dependent on the type coersion
    @classmethod

    def name_validator(cls , value):
        return value.upper()

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


patient_info = {'name' : 'Nischay' , 'email': 'nischay@icici.com'  , 'age' : '21' , 'weight' : 75.58 ,'allergies' : ['Pollen' , 'Dust' , 'Eggs'] , 'contact_details' : {'Phone' : '9876543210'}}

patient_1 = Patient(**patient_info) # Validation is performed here -> type coersion 

insert_patient_data(patient_1)