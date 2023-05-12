def show_homepage():

    print("")
    print("===" + " " + "DonateMe Homepage" + " " + "===")
    print("")
    print("------------------------------------------")
    print("| 1.    Login     | 2.    Register      |")
    print("------------------------------------------")
    print("------------------------------------------")
    print("| 3.    Donate    | 4.    Show Donations |")
    print("------------------------------------------")
    print("------------------------------------------")
    print("              | 5. Exit       |")
    print("------------------------------------------")
    
def donate (username):

    print("")
    donation_amt = input("Enter amount to donate: ")
    donation_string = username + " donated $" + donation_amt
    print("")
    print("Thank you for the donation")
    return donation_string

def show_donations (donations):
    print("")
    print("\n--- All Donations ---")
    if len(donations) == 0:
        print("")
        print("Currently, there are no donations.")
    
    else:

        for donation in donations:

            print("")
            print(donation)
            print("")
