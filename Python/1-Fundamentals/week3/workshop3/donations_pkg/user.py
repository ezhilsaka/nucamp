def login(database, username, password):

    if username in database and database[username] == password:
        print("")
        print("Welcome " + username + " !")
        return username

    elif username in database and database[username] != password:
        print("")
        print("Invalid Password, Please try again")
        return ""

    else:
        print("")
        print("User name not found")
        return ""


def register(database, username):

    if username in database:
        print("")
        print("Username already registered")
        return ""

    else:
        print("")
        print("Registered Successfully")
        return username
