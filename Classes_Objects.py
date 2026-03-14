"""
Python Classes and Ojects
===========================
Instances of a class

"""
class Dog:

    def __init__(self, name, breed):
        self.name = name # Attribute for dog's name
        self.breed = breed # Attribute for dog's breed
    
    def bark(self):
        return f"{self.name} is barking!"
    
    def eat(self, food):
        return f"{self.name} is eating {food}."
    
    def sleep(self):
        return f"{self.name} is sleeping."

my_dog = Dog("Buddy", "Golden Retreiver")
print(my_dog.bark())
print(my_dog.eat("bones"))
print(my_dog.sleep())
    