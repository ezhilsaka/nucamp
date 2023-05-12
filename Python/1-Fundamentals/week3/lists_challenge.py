import random


diamonds = ["AD", "2D", "3D", "4D", "5D", "6D",
            "7D", "8D", "9D", "10D", "JD", "QD", "KD"]
hand = []

while diamonds:
    
    user_choice = input("Press enter to pick a card, or Q to quit: ")

    if user_choice.upper() == "Q":
        print("Your hand: ", hand)
        print("Remaining cards: ", diamonds)
        break

    elif user_choice != "":
        print("Invalid Choice, Please try again")
    
    else:
        card_picked = random.choice(diamonds)
        hand.append(card_picked)
        diamonds.remove(card_picked)
        print("Your hand", hand)
        print("Remaining cards: ", diamonds)

if not diamonds:
    print("There are no more cards to pick")


   






