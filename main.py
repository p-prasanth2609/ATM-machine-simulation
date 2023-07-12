class InsufficientException(Exception):
    pass


class InvalidAmountException(Exception):
    pass


class Atm:
    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            raise InsufficientException("invalid deposit amount")
        self.balance += amount
        print(f"deposited {amount}, new balance: {self.balance}")

    def withdraw(self, amount):
        if amount <= 0:
            raise InsufficientException("invalid withdraw amount")
        if amount > self.balance:
            raise InvalidAmountException("insufficient")
        self.balance -= amount
        print(f"withdrawn {amount}, new balance: {self.balance}")


def main():
    atm = Atm(1000)
    while True:
        print("\nATM MENU")
        print("1. deposit")
        print("2. withdraw")
        print("3. exit")
        option = input("enter the option:")
        if option == '1':
            try:
                amount = float(input("enter the deposit amount:"))
                atm.deposit(amount)
            except ValueError:
                print("invalid input")
        elif option == '2':
            try:
                amount = float(input("enter the withdraw amount:"))
                atm.withdraw(amount)
            except ValueError:
                print("invalid input")
            except InsufficientException as e:
                print(e)
            except InvalidAmountException as e:
                print(e)

        elif option == '3':
            print("**** Thank you ****")
            break


if __name__ == "__main__":
    main()
