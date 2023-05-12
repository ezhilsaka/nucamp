# User class for the bank app

class User:

    def __init__(self, name, pin, password):

        self.name = name
        self.pin = pin
        self.password = password

    def change_name(self):

        while True:

            new_name = input("Enter the new username: ")

            if len(new_name) >= 2 and len(new_name) <= 10:

                self.name = new_name
                break

            else:

                print(" ")
                print(
                    "The user name should be between 2 to 10 characters. Please try again")

    def change_pin(self):

        while True:

            new_pin = input("Enter the new PIN: ")

            if len(new_pin) == 4:

                if not " " in new_pin:

                    if new_pin != str(self.pin):

                        self.pin = new_pin
                        break

                    else:

                        print(" ")
                        print(
                            "The new PIN can't be same as the old PIN. Please try again")

                else:

                    print(" ")
                    print("Space is not allowed for PIN")

            else:

                print(" ")
                print("The PIN should be of length of 4 exactly.")

    def change_password(self):

        while True:

            new_password = input("Enter the new password: ")

            if len(new_password) >= 5:

                self.password = new_password
                break

            else:

                print(" ")
                print(
                    "The password should be of minimum 5 or more characters. Please try again")

# Bank user class inheriting the user class


class BankUser (User):

    def __init__(self, name, pin, password):

        super().__init__(name, pin, password)
        self.balance = 0.00
        self.onhold = False

    def toogle_onhold_status(self):

        return not self.onhold

    def show_balance(self):

        print("{} has an account balance of: ${:.2f}".format(
            self.name, self.balance))

    def withdraw(self, amount):

        onhold_status = self.toogle_onhold_status()

        if onhold_status:

            if not isinstance(amount, str):

                if amount > 0.00:

                    if amount < self.balance:

                        self.balance = self.balance - amount

                else:

                    print(" ")
                    print("The withdrawl money is not valid")

            else:

                print(" ")
                print("The withdrawl money is not valid")

        else:

            print(" ")
            print(
                "The account is on-hold. Transaction can't be done until the hold is released")

    def deposit(self, amount):

        if not isinstance(amount, str):

            if amount > 0.00:

                self.balance = self.balance + amount

            else:

                print(" ")
                print("The deposit money is not valid")

        else:

            print(" ")
            print("The deposit money is not valid")

    def transfer_money(self, user, amount):

        print(" ")
        print("You are transferring ${:.2f} to {}".format(amount, user.name))
        print(" ")
        print("Authentication required")
        user_pin = int(input("Enter your PIN: "))

        if (user_pin) == self.pin:

            if amount < self.balance:

                print(" ")
                print("Transfer Authorized")
                user.deposit(amount)
                self.withdraw(amount)
                return True

            else:

                print(" ")
                print("Insufficient Balance in your account to make a transfer")
                return False

        else:

            print(" ")
            print("Invalid Pin. Transaction canceled")
            return False

    def request_money(self, request_from_user, amount):

        print(" ")
        print("You are requesting ${:.2f} from {}".format(
            amount, request_from_user.name))
        print("User authentication is required")
        print(" ")
        requested_from_user_pin = int(
            input("Enter {}'s PIN: ".format(request_from_user.name)))

        if requested_from_user_pin == request_from_user.pin:

            requesting_user_password = input("Enter your password: ")

            if requesting_user_password == self.password:

                if amount < request_from_user.balance:

                    self.deposit(amount)
                    request_from_user.withdraw(amount)
                    return True

                else:

                    print(" ")
                    print("Insufficent balance in {}'s account to request money".format(
                        request_from_user.name))

            else:

                print(" ")
                print("Invalid Password. Transaction cancelled")
                return False

        else:

            print(" ")
            print("Invalid Pin. Transaction cancelled")
            return False

# Driver Code for Task 4


user1 = BankUser("Bob", 1234, "password")
user2 = BankUser("Bobby", 4321, "newpassword")
user1.deposit(4000.00)
print(" ")
print("User 1 Name is: {}, PIN is : {}, Password is: {}, and Balance is: {:.2f}.".format(
    user1.name, user1.pin, user1.password, user1.balance))
user2.deposit(5000.00)
print(" ")
print("User 2 Name is: {}, PIN is : {}, Password is: {}, and Balance is: {:.2f}.".format(
    user2.name, user2.pin, user2.password, user2.balance))
print(" ")
user1.show_balance()
user2.show_balance()

transfer_status = user2.transfer_money(user1, 500.00)

if transfer_status:

    user1.show_balance()
    user2.show_balance()

    request_money_status = user1.request_money(user2, 250.00)

    if request_money_status:

        print(" ")
        print("Request authorized")
        print("{} sent $250.00".format(user2.name))
        print(" ")
        user1.show_balance()
        user2.show_balance()

    else:

        user1.show_balance()
        user2.show_balance()

else:

    user1.show_balance()
    user2.show_balance()


"""  Driver Code for Task 1

user1 = User("Bob", 1234, "password")
print (user1.name + " " + str(user1.pin) + " " + user1.password)  """

""" Driver Code for Task 2

user1.change_name()
user1.change_pin()
user1.change_password()
print(user1.name + " " + str(user1.pin) + " " + user1.password) """

""" Driver Code for Task 3

user1 = BankUser("Bob", 1234, "password")
print (user1.name + " " + str(user1.pin) + " " + user1.password + " " + str(user1.balance))  """
