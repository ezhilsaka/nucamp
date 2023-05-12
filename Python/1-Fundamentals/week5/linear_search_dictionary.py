def linear_search_dict(the_dict, target):
    
    for col, val in the_dict.items():

        if val == target:

            print("Found at key {}".format(col))
            return
    
    print("The Target is not in the dictionary")
    return -1

my_dict = {"red": 5, "blue": 3, "yellow": 12, "green": 7}
linear_search_dict(my_dict, 5)
linear_search_dict(my_dict, 3)
linear_search_dict(my_dict, 8)