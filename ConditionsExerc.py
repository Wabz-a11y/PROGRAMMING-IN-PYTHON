"""
Exercise:
 A company decided to give a bonus to employee according to following criteria:
 Time period of service     Bonus
 more than 10 years          10%
 >=6 and <=10                 8%
 Less than 6 years            5%

 Ask user for their salary and years of service and print the net bonus amount
"""

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
f=open("C:\\Users\\ianwa\\OneDrive\\Desktop\\UNITS\\3.1\\Programming in Python\\Python Codes\\printInFile.txt", "a")

print (f"Your salary is:  {salary:.2f} and year(s) of servic is: {yearOfService}", file=f)

print(f"Your bonus amount is: Ksh. {bonus:.2f}", file=f)

f.close()

"""

"""
Create a grading system using the following conditions
 Score            Grade
 70 - 100          A
 60 - 69           B
 50 - 59           C
 40 - 49           D
 0 - 39            Fail

 Prompt the user to enter marks for 3 subjects 
 Compute the average 
 Grade average score
"""

print ("Enter marks for 3 subjects.")
marks = []
mark1 = int(input ("Enter marks for subject 1: "))
mark2 = int(input("Enter marks for subject 2: "))
mark3 = int(input("Enter marks for subject 3: "))

marks.append (mark1)
marks.append (mark2)
marks.append (mark3)

average = (mark1 + mark2 + mark3) / 3


if (average >= 70):
    grade = "A"
elif (average >= 60):
    grade = "B"
elif (average >= 50):
    grade = "C"
elif (average >= 40):
    grade = "D"
else :
    grade = "Fail"

print (f"Your average Score is {average:.2f}, and average Grade is: {grade}")
