# a,b=12,13
# print(a+b) 

# def addition(a,b):
#     print(a+b)
# addition(12,13)

# class Calculator:
#     def add(self,a,b):  # is used to store objects location or say detailsself
#         return a+b
# calc = Calculator()
# print(calc.add(12,13))


# class bags:
#     def __init__(self,material,zips,pockets):
#         self.material = material
#         self.zips = zips
#         self.pockets = pockets

# reebok = bags("leather",3,2)
# campus = bags("polyster",2,4)

# print(reebok.material)
# print(campus.zips)



# class Animal:
#     a=12
#     def __init__(self,name):
#         self.name = name
    
#     def hello(self):
#         print(f"how are you my name is {self.name}")

#     @classmethod
#     def details(cls):
#         print(f"how are you my name is {cls.a}")

#     @staticmethod
#     def speak():
#         print(f"Hello how are you I am a static method")

# obj = Animal("lion")
# obj.hello()
# obj.details()
# obj.speak()



# class Animal:
#     a=12
#     def __init__(self,name):
#         self.name = name
    
#     def details(self):
#         print(f"how are you my name is {self.name}")

# class Humans(Animal):
#     pass

# obj= Animal("lion")
# obj2= Humans("Harsh")

# obj.details()
# obj2.details()
# print(obj2.a)

# class robot(Animal):
#     def __init__(self, name,serialNo):
#         super().__init__(name)
#         self.serialNo = serialNo



# # method overriding (we need inheritance)
# class Animal:
#     a = 12
#     def __init__(self,name):
#         self.name = name

#     def details(self):
#         print(f"your name is {self.name}")

# class Humans(Animal):
#     b=12
#     def details(self):
#         super().details()
#         print(f"your info is {self.name} and this is all we have")

# obj = Humans("harsh")
# obj.details() 



# # method overloading for other languages
# class hello:
#     def speak(self,a):
#         print(f"how are you {a}")

#     def speak(self,a,b):
#         print("hello how are you {a},{b}")

# obj = hello()
# obj2 = hello()
# obj.speak(1)      # Output: how are you 1
# obj2.speak(1,2)   # Output: hello how are you 1, 2

# #method overloading for python
# class Hello:
#     def speak(self, a, b=None):
#         if b is None:
#             print(f"how are you {a}")
#         else:
#             print(f"hello how are you {a}, {b}")

# obj = Hello()
# obj.speak(1)      # Output: how are you 1
# obj.speak(1, 2)   # Output: hello how are you 1, 2



#Abstraction
from abc import ABC , abstractmethod

class enforce(ABC):
    @abstractmethod
    def enginestart(self):
        pass

class bike(enforce):
    def enginestart(self):
        pass  

class car(enforce):
    def enginestart(self):
        pass

class truck(enforce):
    def enginestart(self):
        pass

obj1 = bike()
obj2 = car()
obj3 = truck()