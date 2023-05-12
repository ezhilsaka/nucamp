def reverse(str):
    reversed_string = ""
    len_of_str = len(str)
    for i in range(len_of_str-1, -1, -1):
        reversed_string = reversed_string + str[i]
    return reversed_string

name = input("What is your name? ")
print("Your name reversed is:", reverse(name))
