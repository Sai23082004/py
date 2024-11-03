import numpy as np
# Create an array
arr = np.array([5, 8, 3, 12, 7])
# Find the minimum value
min_val = np.min(arr)
# Find the maximum value
max_val = np.max(arr)
# Find the sum of the array
sum_val = np.sum(arr)
# Find the cumulative sum of the array
cum_sum = np.cumsum(arr)
# Output the results
print("Array: ",arr)
print("Minimum value: ",min_val)
print("Maximum value: ",max_val)
print("Sum of the array: ",sum_val)
print("Cumulative sum of the array: ",cum_sum)
# OUTPUT:
# Array:  [ 5  8  3 12  7]
# Minimum value:  3
# Maximum value:  12
# Sum of the array:  35
# Cumulative sum of the array:  [ 5 13 16 28 35]
