def check_key_in_dict(dictionary,key):
    return key in dictionary
fruit_colors = {'Apple': 'Red', 'Banana': 'Yellow', 'Kiwi': 'Green'}
key_to_check = input("Enter a key to check in the dictionary: ")
if check_key_in_dict(fruit_colors, key_to_check):
    print(f'The key "{key_to_check}" exists in the dictionary.')
else:
    print(f'The key "{key_to_check}" does not exist in the dictionary.')

# OUTPUT:
# Enter a key to check in the dictionary: Green
# The key "Green" does not exist in the dictionary.
