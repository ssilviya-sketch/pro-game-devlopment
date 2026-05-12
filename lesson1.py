#object orientated to programming is a style where programs ar built using object each object has attributes(data/variables) and methods(functions)
#object represents real full things like a car,animals
#class is a blueprint or tablet for creating object
#object is a real instance created from a class
class student:
    def __init__(self,name,age):
        self.name = name
        self.age = age
#init is an initializing function where in we give those variables wich we want te create as soon as we create an object
student1 = student("mika","12")
print(student1.name)
print(student1.age)