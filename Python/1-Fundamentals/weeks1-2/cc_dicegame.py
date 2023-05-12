""" import random

high_score = 0


def dice_game():
    
    global high_score

    while True:
        print("Current High Score: ", high_score)
        print("1)" + " Roll Dice")
        print("2)" + " Leave Game")
        user_choice = input("Enter your choice: ")

        if user_choice == "1":
            roll1 = random.randint(1, 6)
            roll2 = random.randint(1, 6)
            total_roll = roll1 + roll2
            print("You roll a... ", roll1)
            print("You roll a... ", roll2)
            print("\n You have rolled a total of: ", total_roll)

            if total_roll > high_score:
                print("New high score!")
                high_score = total_roll
        
        elif user_choice == "2":
            break; 

        else:
            print("invalid choice")
    
dice_game()
 """

for i in [1, 2, 3, 4]:
    print("inside i loop", i)
    if (i > 2):
        break
    for j in [1, 2, 3, 4]:
        if (j > 3):
            break
        print("inside J loop", j)


