"""
Exercise:
 A company decided to give a bonus to employee according to following criteria:
 Time period of service     Bonus
 more than 10 years          10%
 >=6 and <=10                 8%
 Less than 6 years            5%

 Ask user for their salary and years of service and print the net bonus amount
"""

salary = float(input("Please enter your salary: "))
yearOfService = int(input("Enter year(s) of service: "))

if (yearOfService > 10):
    bonus = salary * 0.1
elif (yearOfService >= 6 and yearOfService <= 10):
    bonus = salary * 8
else :
    bonus = salary * 0.5
print(f"Your bonus amount is: Ksh. {bonus:.2f} ")

# Writing into the file Salary, Year of service and Bonus.
f=open("C:\\Users\\ianwa\\OneDrive\\Desktop\\Programming Python\\TestFile.txt", "w")
print (f"Your salary is:  {salary:.2f} and year(s) of servic is: {yearOfService}", file=f)

print(f"Your bonus amount is: Ksh. {bonus:.2f}", file=f)

f.close()