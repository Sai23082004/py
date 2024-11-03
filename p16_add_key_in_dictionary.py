my_dict = {'name': 'Muneera', 'age': 30, 'city': 'New York'}
def add_key_value_pair(dictionary, key, value):
 dictionary[key] = value
new_key = input("Enter a new key: ")
new_value = input("Enter the value for: ")
add_key_value_pair(my_dict, new_key, new_value)
print("Updated Dictionary:", my_dict)

# OUTPUT:
# Enter a new key: college
# Enter the value for 'college': cbit
# Updated Dictionary: {'name': 'Muneera', 'age': 30, 'city': 'New York', 'college': 'cbit'}

