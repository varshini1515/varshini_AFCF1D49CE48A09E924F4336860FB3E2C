class BankAccount:

  def __init__(self, account_number, account_holder_name, initial_balance=0.0):
    self.__account_number = account_number
    self.__account_holder_name = account_holder_name
    self.__account_balance = initial_balance

  def deposit(self, amount):
    if amount > 0:
      self.__account_balance += amount
      print(f"Deposited ${amount}. New balance: ${self.__account_balance}")
    else:
      print("Invalid deposit amount. Please deposit a positive amount.")

  def withdraw(self, amount):
    if amount > 0:
      if amount <= self.__account_balance:
        self.__account_balance -= amount
        print(f"Withdrew ${amount}. New balance: ${self.__account_balance}")
      else:
        print("Insufficient funds. Cannot withdraw.")
    else:
      print("Invalid withdrawal amount. Please withdraw a positive amount.")

  def display_balance(self):
    print(
        f"Account balance for {self.__account_holder_name}: ${self.__account_balance}"
    )


# Example usage:
if __name__ == "__main__":
  # Creating an instance of the BankAccount class
  account1 = BankAccount("123456789", "John Doe", 1000.0)

  # Depositing and withdrawing money
  account1.display_balance()
  account1.deposit(500.0)
  account1.withdraw(200.0)
  account1.display_balance()
