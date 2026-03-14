"""
Write a python function to calculate the area of a rectangle given its length and width
Volume of a cylinder
Grading system


import math

# PI * r^3 * height
def volumeCylinder (radius, height):
    volumeCylinder = math.pi * radius * radius * radius * height
    return volumeCylinder

vol = volumeCylinder (20, 14)
print (vol)
"""

import math

def volumeCylinder (radius, height):
    volume = math.pi * radius * radius * radius * height
    return volume

radius = int(input("Enter radius: "))
height = int(input("Enter height: "))

volume = volumeCylinder(radius, height)
print (f"The volume of the cylinder is: {volume:.2f}")



