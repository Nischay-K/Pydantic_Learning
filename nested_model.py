from pydantic import BaseModel

class Address(BaseModel):

    city: str
    state: str
    pin: str


class Patient(BaseModel):

    name: str
    gender: str
    age: int
    address: Address #This Address class is used as a field in this class!!

address_dict = {'city' : 'Bamgalore' , 'state' : 'Karnataka' , 'pin' : '560040'}
address_1 = Address(**address_dict)

patient_info = {'name' : 'Nischay' , 'gender' : 'Male' , 'age' : '21' , 'address' : address_1}
patient_1 = Patient(**patient_info)

print(patient_1)
print(patient_1.gender)
print(patient_1.address.city)
print(patient_1.address.pin)
print(patient_1.age)
print(patient_1.address.state)


#Benefits of nested Model:

#1. Better organiztion of the related data (e.g., insurance , address , vitals)
#2. Reusability: Use Vitals in multiple models (e.g., Patient , MedicalRecords)
#3. Readability: Easier for developers and API consumers to understand
#4. Validation: Nested Models are validated automatically - that is no extra work needed!!