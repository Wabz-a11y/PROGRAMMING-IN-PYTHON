"""
NAME: IAN WABWIRE
ADM NO.: BSCIT-05-0069/2024
"""
# python variables
name = "John"
age = 13
discount = 10.2
tall = True
x, y, z = "orange", 10, 3.142
a=b=c="Brent"
print ("Discount is:", discount, "and age is:", age)

f = open ("C:\\Users\\ianwa\\OneDrive\\Desktop\\Programming Python\\CreateFile.txt", "a")
print (f"Discount is: {discount:.2f} and age is : {age}", file=f)

f.close()


last_name = input("Enter your name: ")
score = int(input("Enter marks: "))
budget = float(input("Enter budget: "))

print("Last name: ", last_name)
print("Score is: ", score)
print("Budget is: ", budget)

f = open ("C:\\Users\\ianwa\\OneDrive\\Desktop\\Programming Python\\CreateFile.txt", "a")
print("Last name: ", last_name, file=f)
print("Score is: ", score, file=f)
print(f"Budget is: ", budget, file=f)
f.close()


x = "awesome"

def myfunction():
   x = "fantastic"
   print ("They are " + x)
myfunction()

print("It is " + x)
