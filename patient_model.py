from pydantic import BaseModel , EmailStr , AnyUrl , Field
from typing import List , Dict , Optional , Annotated
#Field is used to set/attach the metadata's also!! - Like this helps a lot during API call's(FastAPI)
#Field + Annotated combination helps to set the metadata



class Patient(BaseModel):
    #Only Type validation is done below
    name: str = Annotated[str , Field(max_length = 50 , title = 'Name of the Patient' , description = 'Gives the name of the patient in less than 50 Characters' , examples = ['Nischay' , 'Kunal' , 'Nitish' , 'Monish' , 'Virat'])] #The name can only be of 50 characters
    email: EmailStr #To validate email provided by the user
    linkedIn_url: AnyUrl #To get the url of any webpage or website
    age: int = Field(gt = 0 , lt = 70) #Field is used to provide constraints on the specific field like the age cannot be negative(constraint)
    weight: float = Annotated[float , Field(gt = 0 , strict = True)]  #How many fields are present in the pydantic are required to be passed when as object is created and the strict does no allow the pydantic to do the type coersion
    married: Annotated[Optional[bool] , Field(default = None , description = 'Is the patient married or not')] #Field is also used to add the default values as well!!!
    allergies: Annotated[Optional[List[str]] , Field(default = None , max_length = 5)] #This field may or may not be instantiated during the object that is they do not throw an error and a ddefault value should be given as None because no values will be assummed before hand
    contact_details: Dict[str , str]

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



#Pydantic has a special feature where it automatically converts it into integer
patient_info = {'name' : 'Nischay' , 'email': 'nischay@gmail.com' , 'linkedIn_url' : 'http://linkedin.com/125846325' , 'age' : '21' , 'weight' : 75.58 ,'allergies' : ['Pollen' , 'Dust' , 'Eggs'] , 'contact_details' : {'Phone' : '9876543210'}} 


patient_1 = Patient(**patient_info) #**to unwrap the dictionary items it's called as the **kwargs

update_patient_data(patient_1)