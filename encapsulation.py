"""
Inheritance
Encapsulation in Python

protected: self._protected = protected (Accessible outside the class but not allowed)
private:  self.__private = private (Not accessible outside the class)
public: self.public = public (Accessible)

class BankAccount:
    def __init__(self, balance, name, acc_no):
        self._balance = balance # Private attribute
        self._name = name # Protected attribute
        self.acc_no = acc_no # Public attribute
    

    def deposit(self, amount):
        self._balance += amount
        return f"New Balance: {self._balance}"
    
    def _deposit(self, amount):
        self._balance += amount
        return f"New Balance: {self._balance}"
    
    def get_balance(self):
        return self._balance

account = BankAccount(1000, "Wabz", "AZ735637")

print(account.get_balance()) # Allowed
print(account._balance) # Error: Attribut is private

print(account._deposit(2000))
print(account._name)
print(account.acc_no)
"""

