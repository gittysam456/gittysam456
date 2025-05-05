#create a class name atm divides a menu driven interface to perform basic banking operations such as set pin, check balance and deposit and withdraw-money
"""class Atm:
    def __init__(self):
        self.pin = ""
        self.balance = 0.0

    def set_pin(self, pin):
        self.pin = pin
        print("PIN set successfully.")

    def check_balance(self):
        print(f"Your balance is: {self.balance}")

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited: {amount}")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrawn: {amount}")
        else:
            print("Invalid withdrawal amount or insufficient balance.")
    def menu(self):
        while True:
            print("\nATM Menu:")
            print("1. Set PIN")
            print("2. Check Balance")
            print("3. Deposit")
            print("4. Withdraw")
            print("5. Exit")

            choice = input("Enter your choice: ")

            if choice == '1':
                pin = input("Enter new PIN: ")
                self.set_pin(pin)
            elif choice == '2':
                self.check_balance()
            elif choice == '3':
                amount = float(input("Enter amount to deposit: "))
                self.deposit(amount)
            elif choice == '4':
                amount = float(input("Enter amount to withdraw: "))
                self.withdraw(amount)
            elif choice == '5':
                print("Exiting ATM.")
                break
            else:
                print("Invalid choice. Please try again.")
t=Atm()
print("Welcome to ATM")
t.menu()"""
class ATM:
   def __init__(self):
       self.balance = 0
       self.pin = ''
       self.menu()
   def menu(self):
         while True:
              print("\nATM Menu:")
              print("1. Set PIN")
              print("2. Check Balance")
              print("3. Deposit")
              print("4. Withdraw")
              print("5. Exit")

              choice = input("Enter your choice: ")

              if choice == '1':
                self.set_pin()
              elif choice == '2':
                self.check_balance()
              elif choice == '3':
                self.deposit()
              elif choice == '4':
                self.withdraw()
              elif choice == '5':
                print("Exiting ATM.")
                break
              else:
                print("Invalid choice. Please try again.")

         def check_balance(self):
             print(f"Your balance is: {self.balance}")

         def deposit(self, amount):
             if amount > 0:
                 self.balance += amount
                 print(f"Deposited: {amount}")
                 self.Balance()
             else:
                 print("Invalid deposit amount.")

         def withdraw(self, amount):
             if 0 < amount <= self.balance:
                 self.balance -= amount
                 print(f"Withdrawn: {amount}")
             else:
                 print("Invalid withdrawal amount or insufficient balance.")

bov=ATM()
print("Welcome to ATM")
bov.menu()