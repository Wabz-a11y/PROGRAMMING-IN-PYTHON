# Raising Exceptions manually

def withdraw (amount):
   if amount < 0:
     raise ValueError("Amount cannot be negative")
   print(f"Withdrawn {amount}.")

try:
   withdraw(500)
except ValueError as e:
 print(f"Transaction failed: {e}.")