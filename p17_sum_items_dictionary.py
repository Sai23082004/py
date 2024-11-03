my_dict = {'a': 10, 'b': 20, 'c': 30, 'd': 40}
def sum_dictionary_items(dictionary):
 return sum(dictionary.values())
total_sum = sum_dictionary_items(my_dict)
print(f"Sum of all items in the dictionary: {total_sum}")

# OUTPUT:
# Sum of all items in the dictionary: 100
