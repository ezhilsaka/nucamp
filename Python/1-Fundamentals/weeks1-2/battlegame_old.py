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

exit_code = 0

# Getting input from the user

while True:

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
        print("\nYour have chosen the characeter: ", character)
        print("Health: ", my_hp)
        print("Damage: ", my_damage)
        break
    elif character == "2" or character.lower() == "elf":
        character = elf
        my_hp = elf_hp
        my_damage = elf_damage
        print("\nYour have chosen the characeter: ", character)
        print("Health: ", my_hp)
        print("Damage: ", my_damage)
        break
    elif character == "3" or character.lower() == "human":
        character = human
        my_hp = human_hp
        my_damage = human_damage
        print("\nYour have chosen the characeter: ", character)
        print("Health: ", my_hp)
        print("Damage: ", my_damage)
        break
    elif character == "4" or character.lower() == "orc":
        character = orc
        my_hp = orc_hp
        my_damage = orc_damage
        print("\nYour have chosen the characeter: ", character)
        print("Health: ", my_hp)
        print("Damage: ", my_damage)
        break
    elif character == "5":
        print("Exiting the Game")
        exit_code = 1
        break
    else:
        print("Unknown Character")

# Battle with Dragon

while exit_code == 0:

    dragon_hp = dragon_hp - my_damage
    print("\nThe " + character + " damaged the Dragon!")
    print("The Dragon's hitpoints are now: ", dragon_hp)

    if dragon_hp <= 0:
        print("\nThe Dragon has lost the battle")
        break

    my_hp = my_hp - dragon_damage
    print("\nThe Dragon strikes back at ", character)
    print("The " + character + " hitpoints are now: ", my_hp)

    if my_hp <= 0:
        print("\nThe " + character + " has lost the battle")
        break
