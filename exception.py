"""
Exception handling


try:
    result = 10/0

except Exception as e :
    print(f"An error occurred: {e}")
"""

# Handling the different erros separately
try :
    num = int(input("Enter a number: "))
    result = 10 / num

except ValueError:
    print("Invalid input! Please enter  a number.")
except ZeroDivisionError:
    print("Cannot divide by zero!")

else:
    print(f"The value is: {result:.2}")
finally:
    print("The program successfully executed!")