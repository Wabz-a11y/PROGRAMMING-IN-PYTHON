"""
NAME: IAN WABWIRE
ADM NO.: BSCIT-05-0069/2024

Exercise 1

# Write a program to prompt the user for hours and rate per hour t0 compute gross pay.
(Gross_pay=hours_worked*rate_per_hour)

Output:
     Enter Hours:35
     Enter Rate: 2.75
     Gross Pay: 96.25

"""
hours = int(input("Enter Hours: "))
rate = float(input("Enter Rate: "))
# gross = float(input("Gross Pay: "))

hours_worked = hours
rate_per_hour = rate
Gross_pay = hours_worked * rate_per_hour

print ("Gross Pay: ", Gross_pay)


import math

"""
Exercise 2
Write a python program that reads the radius of a sphere and calculates the volume. Volume = 4/3PIr3
"""

PI = 3.142
radius = int(input("Enter radius: "))

Volume = 4/3 * PI * radius * radius * radius

print (f"Volume is: {Volume:.2f}")