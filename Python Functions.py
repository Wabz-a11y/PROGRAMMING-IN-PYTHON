# Python Functions

"""
User Defined Functions

# A function with no parameters
def myName ():
    print ("My name is Wabz.")
# Function call
myName()

# A function with parameters
def sum(a,b):
    sum = a + b
    return sum
c = sum (7,8)
print (c)

name = input("Enter your name: ")
age = int(input("Your age: "))

def myDetails (name, age):
    # print ("My name is "+name+" and I'm "+str(age)+" years old.")
    print (f"My name is {name}, and I'm {age} years old.")

myDetails (name, age)


def myDetails (name, age = 65):
    # print ("My name is "+name+" and I'm "+str(age)+" years old.")
    print (f"My name is {name}, and I'm {age} years old.")

my_Name = input("Enter your name: ")
my_Age = int(input("Your age: "))

myDetails (my_Name, my_Age)
"""

# Defining a function
def myFunction (items):
    # for x in items:
    #    print (x)
    
    for key, value in items.items():
        print (key, value)

# Passing parameters    
cars = ["Audi", "Mazda", "Range Rover", "Chevrolet"]
studentDetails = {
    "Name" : "Wabz",
    "Age" : 34,
    "DoB" : 2009
}
# Calling a function
myFunction (studentDetails)

