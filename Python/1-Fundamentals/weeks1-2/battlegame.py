# Defining Game Character and their Stats

wizard = "Wizard"
elf = "Elf"
orc = "Orc"
human = "Human"

wizard_hp = 70
elf_hp = 100
orc_hp = 120
human_hp = 150
dragon_hp = 300

wizard_damage = 150
elf_damage = 100
orc_damage = 200
human_damage = 20
dragon_damage = 50

# Variables required to exit and restat the game
exit_code = 0
game_start = "y"

# Getting input from the user

while game_start.lower() == "y":

    print("1)" + " " + "Wizard")
    print("2)" + " " + "Elf")
    print("3)" + " " + "Human")
    print("4)" + " " + "Orc")
    print("5)" + " " + "Exit the game")

    character = input("Choose your character:")

    if character == "1" or character.lower() == "wizard":
        character = wizard
        my_hp = wizard_hp
        my_damage = wizard_damage
        exit_code = 0
    elif character == "2" or character.lower() == "elf":
        character = elf
        my_hp = elf_hp
        my_damage = elf_damage
        exit_code = 0
    elif character == "3" or character.lower() == "human":
        character = human
        my_hp = human_hp
        my_damage = human_damage
        exit_code = 0
    elif character == "4" or character.lower() == "orc":
        character = orc
        my_hp = orc_hp
        my_damage = orc_damage
        exit_code = 0
    elif character == "5":
        print("Exiting the Game")
        exit_code = 1
        break
    else:
        print("Unknown Character")
        break
    print("\nYour have chosen the characeter: ", character)
    print("Health: ", my_hp)
    print("Damage: ", my_damage)

# Battle with Dragon

    while exit_code == 0:

        dragon_hp = dragon_hp - my_damage
        print("\nThe " + character + " damaged the Dragon!")
        print("The Dragon's hitpoints are now: ", dragon_hp)

        if dragon_hp <= 0:
            print("\nThe Dragon has lost the battle")
            game_start = input(
                "Do you want to restart the game, enter y or n: ")
            if game_start.lower() == "n":
                print("Exiting the Game")
                break
            elif game_start.lower() == "y":
                wizard_hp = 70
                elf_hp = 100
                orc_hp = 120
                human_hp = 150
                dragon_hp = 300
                wizard_damage = 150
                elf_damage = 100
                orc_damage = 200
                human_damage = 20
                dragon_damage = 50
                exit_code = 1
                continue
            else:
                print("Invalid Entry, Exiting the Game")
                break

        my_hp = my_hp - dragon_damage
        print("\nThe Dragon strikes back at ", character)
        print("The " + character + " hitpoints are now: ", my_hp)

        if my_hp <= 0:
            print("\nThe " + character + " has lost the battle")
            game_start = input(
                "Do you want to restart the game, enter Y or N: ")
            if game_start.lower() == 'n':
                print("Exiting the Game")
                break
            elif game_start.lower() == 'y':
                wizard_hp = 70
                elf_hp = 100
                orc_hp = 120
                human_hp = 150
                dragon_hp = 300
                wizard_damage = 150
                elf_damage = 100
                orc_damage = 200
                human_damage = 20
                dragon_damage = 50
                exit_code = 1
                continue
            else:
                print("Invalid Entry, Exiting the Game")
                break
