"""
Exercise class

Create a class named Temperature. Make two metthods:
   i. convertFahrenheit - it will take celsius and will print it into Fahrenheit.
   ii. convertCelsius - it will take Fahrenheit and will convert it into Celsius.

Create a python class named Circle and normalize it with radius. Create two methods 
   that will compute the area (PI* r2) and the circumference (PI * D) of a circle.

"""
# =====================================================
   # TEMPERATURE CONVERSIONS (FEHRENHEIT AND CELSIUS)
# =====================================================
class Temperature:
    def __init__(self, fahrenheit, celsius):
        self.fahrenheit = fahrenheit
        self.celsius = celsius
    
    def convert_to_Fahrenheit(self):
        # F = (C * 9\5) + 32
        converted = ((self.celsius * 9/5) + 32)
        return f"Celsius to Fahrenheit is: {converted} F."
    
    def convert_to_Celsius(self):
        # C = (F - 32) * 5\9
        converted = ((self.fahrenheit - 32) * 5/9)
        return f"Fehrenheit to Celsius is: {converted:.2f} C."

conversions = Temperature(60, 83)
print(conversions.convert_to_Fahrenheit())
print(conversions.convert_to_Celsius())

# ================================================
   # AREA AND CIRCUMFERENCE OF A CIRCLE 
#===============================================
from math import pi, pow
class Circle:
    def __init__(self, radius):
        self.radius = radius
    
    def Area(self):
        area = pi * pow(self.radius, 2)
        return f"The area is {area:.2f}."
    
    def Circumference(self):
        circumference = pi * (self.radius *2)
        return f"The circumference is {circumference:.2f}"

circle_Radius = Circle(5)
print(circle_Radius.Area())
print(circle_Radius.Circumference())

