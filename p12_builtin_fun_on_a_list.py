def builtin_functions(my_list):
    # 1. len() - Get the length of the list
    length = len(my_list)
    print("Length of the list: ",length)

    # 2. max() - Get the maximum value in the list
    max_value = max(my_list)
    print("Maximum value in the list: ",max_value)

    # 3. min() - Get the minimum value in the list
    min_value = min(my_list)
    print("Minimum value in the list: ",min_value)

    # 4. sum() - Get the sum of all values in the list
    total_sum = sum(my_list)
    print("Sum of all values in the list: ",total_sum)

    # 5. sorted() - Get a sorted version of the list
    sorted_list = sorted(my_list)
    print("Sorted list: ",sorted_list)

my_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
builtin_functions(my_list)


# OUTPUT:
# Length of the list:  11
# Maximum value in the list:  9
# Minimum value in the list:  1
# Sum of all values in the list:  44
# Sorted list:  [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9]
