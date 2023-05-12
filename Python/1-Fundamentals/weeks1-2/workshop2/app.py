from banking_pkg import account

# function to display the menu for ATM


def atm_menu(name):
    print("")
    print("Welcome " + name)
    print("------------------------------------------")
    print("| 1.    Balance     | 2.    Deposit      |")
    print("------------------------------------------")
    print("------------------------------------------")
    print("| 3.    Withdraw    | 4.    Change Pin   |")
    print("------------------------------------------")
    print("------------------------------------------")
    print("| 5. Transfer Funds | 6.    Logout       |")
    print("------------------------------------------")
    print("")

# main program starts


print("")
print("          === Automated Teller Machine ===          ")
print("")

balance = 0.0
registration_name_flag = True
registration_pin_flag = True

# getting the user name and validating it

while (registration_name_flag):

    name = input("Enter name to register: ")
    registration_name_flag = account.name_validation(name)

# getting the pin and validating it

while (registration_pin_flag):

    pin = input("Enter PIN: ")
    registration_pin_flag = account.pin_validation(pin)

print("")
print("Registration Successful !!")
print(name + " has been registered with a starting balance of " + str(balance))

# Login page

while True:

    print("")
    print("LOGIN")
    name_to_validate = input("Enter Name: ")
    pin_validate = input("Enter Pin: ")

    if name_to_validate == name and pin_validate == pin:
        print("")
        print("Login sucessful!")
        break
    else:
        print("")
        print("Invalid Credentials!, Please try again")

# User options

while True:

    atm_menu(name)
    option = input("Choose an option: ")

    if option == "1":
        account.show_balance(balance)

    elif option == "2":
        balance = account.deposit(balance)
        account.show_balance(balance)

    elif option == "3":
        balance = account.withdraw(balance)
        account.show_balance(balance)

    elif option == "4":
        pin = account.change_pin(pin)

    elif option == "5":
        balance = account.transfer_funds(balance)
        account.show_balance(balance)

    elif option == "6":
        account.logout(name)
        break

    else:
        print("")
        print("Please enter valid option")
