def binary_search (the_list, target):

    lower_bound = 0
    upper_bound = len(the_list) - 1
    

    while lower_bound <= upper_bound:

        pivot_index = (lower_bound + upper_bound) // 2
        pivot_value = the_list[pivot_index]

        if pivot_value == target:

            return pivot_index
        
        if pivot_value > target:

            upper_bound = pivot_index - 1
        
        else:

            lower_bound = pivot_index + 1
    
    return -1

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(binary_search(my_list, 10))
print(binary_search(my_list, 4))
print(binary_search(my_list, 33))

