import random

#1. Guessing randon number by user
def guess_random_number(tries, start, stop):

    random_number = random.randint(start, stop)
    user_guess_list = []

    while tries != 0:

        print("The number of tries remaining is {}".format(tries))
        user_guess = int(input("Guess a number between {} and {}: ".format(start, stop)))
        
        # To restrict user from guessing the same number again
        if user_guess in user_guess_list:

            print("This number is already been guessed, guess some other number")
            continue
        
        else:
            
            user_guess_list.append(user_guess)

        # Check to make sure that user is guessing the number within the defined range
        if user_guess > stop or user_guess < start:

            print("Enter the number within the range of {} and {}:".format(start, stop))
            continue

        if user_guess == random_number:

            print("You guessed it !!")
            break
        
        elif user_guess < random_number:

            print("Guess higher than this")
        
        elif user_guess > random_number:

            print("Guess Lower !")
        
        tries -= 1

        if tries == 0:

            print("You reached the maximum number of tries. You failed to guess the number {}".format(random_number))

# 2. System guessing the number using linear search
def guess_random_num_linear(tries, start, stop):

    random_number = random.randint(start, stop)

    for number in range(start, stop + 1):

        if number == random_number:

            print("System guessed it right !!. The number is {}".format(random_number))
            break

        elif number < random_number:

            print("The target number is higher than the number {} system guessed it".format(number))

        elif number > random_number:

            print("The target number is lower than the number {} system guessed it".format(number))

        tries -= 1

        if tries == 0:

            print("System reached the maximum number of tries. System failed to guess the number {}".format(random_number))
            break

# 3. System guessing number using Binary Search 
def guess_random_num_binary(tries, start, stop):

    random_number = random.randint(start, stop)
    lower_bound = start
    upper_bound = stop

    while tries != 0:

        pivot_value = (lower_bound + upper_bound) // 2

        if pivot_value == random_number:

            print("System guessed it right !!. The number is {}".format(random_number))
            break
        
        elif pivot_value > random_number:

            upper_bound = pivot_value - 1
            print("The target number is lower than the number {} system guessed it".format(pivot_value))
        
        elif pivot_value < random_number:

            lower_bound = pivot_value + 1
            print("The target number is higher than the number {} system guessed it".format(pivot_value))

        tries -= 1

        if tries == 0:
            
            print("System reached the maximum number of tries. System failed to guess the number {}".format(random_number))
            break


""" Driver code to test guess_random_number

guess_random_number(5, 0, 10) """

""" Driver code to test guess_random_number in linear search

guess_random_num_linear(5, 0, 10) """

#Driver code to test guess_random_number in binary search 

#guess_random_num_binary(5, 0, 10)

print("Number Guessing Game !!")
print("-----------------------")
print("")
no_of_tries = int(input("Enter the number of tries that you want to try: "))
start_num = int(input("Enter the start number of the range that you want to guess: "))

while True:

    stop_num = int(input("Enter the stop number of the range that you want to guess: "))
    
    if stop_num <= start_num:

        print("The stop number can't be lesser than the start number. Please try again")
    
    else:

        break

print("")
print("Select any one of the below methods available to play the guessing game")
print("")
print("1 - If you want to the guess the number")
print("2 - If you want the system to guess the number using linear search")
print("3 - If you want the system to guess the number using binary search")
print("")
user_choice = input("Enter your choice as 1 or 2 or 3: ")
print("")

if user_choice == '1':

    guess_random_number(no_of_tries, start_num, stop_num)
 
elif user_choice == '2':

    guess_random_num_linear(no_of_tries, start_num, stop_num)

elif user_choice == '3':

    guess_random_num_binary(no_of_tries, start_num, stop_num)

else:

    print("Invalid Choice")
