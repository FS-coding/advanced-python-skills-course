"""
Bank accounts
In this exercise, we will be creating a BankAccount class.

This class must have a constructor that receives an initial amount 
and set it to a property called balance. 
If you don't provide an initial amount, then you should set balance with zero.

You should write a setter and a getter for this property.

The setter should validate if the amount you pass 
is greater than or equal to zero. If it is negative, 
the balance should be setted to zero.
"""

class BankAccount:
    def __init__(self, initial_amount=0):
        self.__balance = initial_amount  # Double underscore for private attribute

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, amount):
        if amount <= 0:
            self.__balance = 0
        else:
            self.__balance = amount


account_1 = BankAccount()
account_2 = BankAccount(100)
account_3 = BankAccount(-100)

print("Initial balance")
print(account_1.balance)
print(account_2.balance)
print(account_3.balance)

print()
print("Setting new balances directly")
account_1._balance = -10
account_2._balance = 1000
account_3._balance = 0
print(account_1.balance)
print(account_2.balance)
print(account_3.balance)

print()
print("Setting new balances (addition)")
account_1.balance = account_1.balance + 1   # Output: 0
account_2.balance = account_2.balance + 1   # Output: 0
account_3.balance = account_3.balance + 1   # Output: 0
print(account_1.balance)
print(account_2.balance)
print(account_3.balance)


