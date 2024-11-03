import numpy as np

# Create a sample NumPy array
arr = np.array(["apple", "banana", "cherry", "date", "elderberry", "fig", "grape"])

# Basic slicing
sliced_arr = arr[1:5]  # Slicing elements from index 1 to 4
print("Sliced Array:", sliced_arr)

# Integer indexing
indexed_arr = arr[[0, 2, 4]]  # Indexing specific elements by integer positions
print("Integer Indexed Array:", indexed_arr)

# Boolean indexing
bool_index = np.array([True, False, True, False, True, False, True])
bool_indexed_arr = arr[bool_index]  # Selecting elements where condition is True
print("Boolean Indexed Array:", bool_indexed_arr)
# OUTPUT:
# Sliced Array: ['banana' 'cherry' 'date' 'elderberry']
# Integer Indexed Array: ['apple' 'cherry' 'elderberry']
# Boolean Indexed Array: ['apple' 'cherry' 'elderberry' 'grape']
