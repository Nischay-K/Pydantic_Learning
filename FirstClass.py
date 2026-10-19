# class Factory:
    # def __init__(self , material , zips , pocket):
        # self.material = material
        # self.zips = zips
        # self.pocket = pocket
# 
    # def show(self):
        # print(f"The material is {self.material} and the number of zips are {self.zips} and the number of pockets are {self.pocket}")
# 
# reebok = Factory("Leather" , 3 , 3)
# campus = Factory("Nylon" , 2 , 3)
# 
# reebok.show()

# class Animal:
    # def __init__(self , age):
        # self.age = age
# 
    # def show(self):
        # print(f"The age is given as {self.age}")
# 
    # @classmethod
    # def hello(cls):
        # print("How are you guys!!")
# 
    # @staticmethod
    # def static():
        # print("I'm a static method call")
# 
# animal = Animal(12)
# 
# animal.show()
# animal.hello()
# animal.static()
# 
# class Animal:
    # def __init__(self , name):
        # self.name = name
# 
    # def show(self):
        # print(f"The name of the respective is {self.name}")
# 
# class Human(Animal):
    # def __init__(self , name , age):
        # super().__init__(name)
        # self.age = age 
    # 
    # def show(self):
        # print(f"The name of the respective is {self.name} and the age is {self.age}")
# animal = Animal("Lion")
# person1 = Human("Nischay" , 22)
# 
# animal.show()
# person1.show()

# class Factory:
    # def __init__(self , material , zips):
        # self.material = material
        # self.zips = zips
# 
    # def show(self):
        # print(f"The material used is {self.material} and number of zips are {self.zips}")
# 
# class BhopalFactory(Factory):
    # def __init__(self ,  material , zips , color):
        # super().__init__(material , zips)
        # self.color = color
    # 
    # def show(self):
        # print(f"The material used is {self.material} and number of zips are {self.zips} and the color is {self.color}")
# 
# class PuneFactory(BhopalFactory):
    # def __init__(self , material , zips , color , pocket):
        # super().__init__(material , zips , color)
        # self.pocket = pocket
    # 
    # def show(self):
        # print(f"The material used is {self.material} and number of zips are {self.zips} and the color is {self.color} and the number of pockets are {self.pocket}")
# 
# 
# f = Factory("Leather" , 5)
# bf = BhopalFactory("Nylon" , 3 , "red")
# pf = PuneFactory("Good Leather" , 5 , "Burgandy" , 2) 
# 
# 
# f.show()
# bf.show()
# pf.show()


# class Demo:
    # def __init__(self):
        # self.name = "Public Member"  #Public
        # self._age = 22  #Protected
        # self.__salary = 50000  #Private
# 
    # def show(self):
        # print("Inside the classes ")
        # print("Name : ", self.name)
        # print("Age : ", self._age)
        # print("Salary : ",self.__salary)
# 
# demo = Demo()
# demo.show()

# from abc import ABC , abstractmethod
# class abstract(ABC):
    # @abstractmethod
    # def parameter(self):
        # pass
    # @abstractmethod
    # def area(self):
        # pass
# 
# class Square(abstract):
    # def __init__(self , side):
        # self.side = side
    # def parameter(self):
        # pass
    # def area(self):
        # pass
# 
# 
# class Circle(abstract):
    # def __init__(self , radius):
        # self.radius = radius
    # def parameter(self):
        # pass
    # def area(self):
        # pass
# 
# obj = Circle(7)

# class Animal:
    # def __init__(self , name , age):
        # self.name = name
        # self.age = age
# 
    # def __str__(self):
        # return f"The given name is : {self.name}"
# 
    # def __add__(self , other):
        # return f"The sum of the ages of two animals is : {self.age}"
# 
# ob = Animal("Lion" , 22)
# ob2 = Animal("Dolphin" , 13)
# print(ob + ob2)


