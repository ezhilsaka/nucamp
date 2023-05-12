def show_balance(balance):

    print("")
    print("Your Current Balance is " + "$" + str(balance))


def deposit(balance):

    while True:
        
        amount_to_deposit = input("Enter amount to deposit/transfer in: ")
        
        if amount_to_deposit == "" or float(amount_to_deposit) <= 0:
            print("Invalid deposit/transfer in amount, please try again")
            continue
        else:
            break
    
    new_balance = balance + float(amount_to_deposit)
    return new_balance


def withdraw(balance):

    while True:
        
        amount_to_withdraw = input("Enter amount to withdraw/transfer out: ")
        
        if amount_to_withdraw == "" or float(amount_to_withdraw) <= 0:
            print("Invalid withdrawl/transfer out amount, please try again")
            continue
        else:
            break

    if float(amount_to_withdraw) > balance:
        print("")
        print("Insufficient Balance. You are trying to withdraw/transfer out more than your current balance")
        return balance

    else:
        new_balance = balance - float(amount_to_withdraw)
        return new_balance


def logout(name):

    print("")
    print("You are loggin out " + "Goodbye " + name + "!")


def name_validation(name):

    registration_flag = True

    if len(name) < 1 or len(name) > 10:
        print("")
        print("The name should be of length between 1 to 10 for registration, Please try again")
        return registration_flag

    registration_flag = False
    return registration_flag


def pin_validation(pin):

    registration_flag = True

    if len(pin) != 4:
        print("")
        print("The pin length should be of length 4, Please try again")
        return registration_flag

    registration_flag = False
    return registration_flag


def change_pin(pin):

    while True:

        current_pin = input("Enter your current pin: ")

        if current_pin == pin:
            new_pin = input("Enter new pin: ")
            pin_validation_flag = pin_validation(new_pin)

            if pin_validation_flag == True:
                print("")
                print("Pin change not successful, Please try again")
                continue

            new_pin_confirmation = input("Re-enter to confirm your new pin: ")

            if new_pin == new_pin_confirmation:
                print("")
                print("Pin chage Successful")
                return new_pin

            else:
                print("")
                print("The pin's are not matching, Please try again")

        else:
            print("")
            print("Your current pin is wrong, Please try again")


def transfer_funds(balance):

    transfer_type = input("Enter 1 for Transfer out and 2 for Transfer in: ")
    initial_balance = balance

    if transfer_type == "1":

        account_to_transfer = input("Enter the account number to transfer: ")
        balance_after_tranfer = withdraw(initial_balance)

        if initial_balance == balance_after_tranfer:
            print("")
            print("Transfer Unsuccessful, please try again")
            return initial_balance

        else:
            print("")
            print("Transfer successful !!")
            return balance_after_tranfer

    elif transfer_type == "2":

        account_from_transfer = input("Enter the transfer from account number: ")
        balance_after_tranfer = deposit(initial_balance)

        print("")
        print("Transfer successful !!")
        return balance_after_tranfer
    
    else:

        print("")
        print("Invalid entry for transfer type, please try again")
        return initial_balance