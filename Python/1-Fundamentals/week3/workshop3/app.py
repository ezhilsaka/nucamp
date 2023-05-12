from donations_pkg import homepage
from donations_pkg.user import login, register

database = {'admin': 'password123'}
donations = []
authorized_user = ""

homepage.show_homepage()

while True:

    print("")
    choice = input("Choose an option: ")
    print("")

    if choice == "1":
        username = input("Enter Username: ")
        password = input("Enter Password: ")
        authorized_user = login(database, username, password)
        homepage.show_homepage()

        if authorized_user != "":
            print("Logged in as: ", authorized_user)
        
    elif choice == "2":
        username = input("Enter Username: ")
        password = input("Enter Password: ")
        authorized_user = register(database, username)
        
        if authorized_user != "":
            database[username] = password

        homepage.show_homepage()

    elif choice == "3":
        
        if authorized_user == "":
            print("You are not logged in")
        
        else:
            donation_string = homepage.donate(authorized_user)
            donations.append(donation_string)

        homepage.show_homepage()
        
        if authorized_user != "":
            print("Logged in as: ", authorized_user)

    elif choice == "4":
        
        if authorized_user == "":
            print("You are not logged in")
        
        else:
            homepage.show_donations(donations)

        homepage.show_homepage()
        
        if authorized_user != "":
            print("Logged in as: ", authorized_user)

    elif choice == "5":
        print("Thank you for using Donation app. Please visiti again !!")
        print("")
        break
    
    else:
        print("Invalid Choice Entered, Please try again")
        print("")
        break