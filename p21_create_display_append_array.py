import array

# Since the array module does not support a 'str' type code directly, 
# we use a list instead to demonstrate similar operations.
# Creating a list of strings
array_items = ["car", "bike", "crane", "bicycle", "bus"]

# Display the list
print("Original list:", array_items)

# Append an item to the list
array_items.append("Auto")
print("New list:", array_items)

# Insert an item at a specific position
array_items.insert(2, "Truck")  # Insert 'grape' at index 2
print("After inserting item:", array_items)

# Reverse the order of the list
array_items.reverse()
print("After reversing:", array_items)
# Another example:
#import all the functions from array library
from array import array
#i is a type code for integer values
array_num=array('i',[1,3,5,3,7,1,9])
print("Original array:",array_num)
array_num.append(11)
print("New array:",array_num)
array_num.insert(2,15)
print("After inserting array:",array_num)
array_num.reverse()
print("Reverse the order of the items:",array_num)
# output:
# Original list: ['car', 'bike', 'crane', 'bicycle', 'bus']
# New list: ['car', 'bike', 'crane', 'bicycle', 'bus', 'Auto']
# After inserting item: ['car', 'bike', 'Truck', 'crane', 'bicycle', 'bus', 'Auto']
# After reversing: ['Auto', 'bus', 'bicycle', 'crane', 'Truck', 'bike', 'car']
# Another Output:
# Original array: array('i', [1, 3, 5, 3, 7, 1, 9])
# New array: array('i', [1, 3, 5, 3, 7, 1, 9, 11])
# After inserting array: array('i', [1, 3, 5, 3, 7, 1, 9, 11, 5])
# Reverse the order of the items: array('i', [5, 11, 9, 1, 7, 3, 5, 3, 1])
