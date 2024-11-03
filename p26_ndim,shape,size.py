import numpy as np

# Creating a 1D array
arr1 = np.array([5, 10, 15])

# Creating a 2D array
arr2 = np.array([[7, 14, 21], [28, 35, 42]])

# Creating a 3D array
arr3 = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])

# Demonstrating properties for the 1D array
print("1D Array:", arr1)
print("ndim:", arr1.ndim)  # Number of dimensions
print("shape:", arr1.shape)  # Shape of the array
print("size:", arr1.size)  # Total number of elements
print("dtype:", arr1.dtype)  # Data type of elements

print("\n---\n")

# Demonstrating properties for the 2D array
print("2D Array:\n", arr2)
print("ndim:", arr2.ndim)
print("shape:", arr2.shape)
print("size:", arr2.size)
print("dtype:", arr2.dtype)

print("\n---\n")

# Demonstrating properties for the 3D array
print("3D Array:\n", arr3)
print("ndim:", arr3.ndim)
print("shape:", arr3.shape)
print("size:", arr3.size)
print("dtype:", arr3.dtype)
# OUTPUT:
# 1D Array: [ 5 10 15]
# ndim: 1
# shape: (3,)
# size: 3
# dtype: int64

# ---

# 2D Array:
#  [[ 7 14 21]
#  [28 35 42]]
# ndim: 2
# shape: (2, 3)
# size: 6
# dtype: int64

# ---

# 3D Array:
#  [[[1 2]
#   [3 4]]

#  [[5 6]
#   [7 8]]]
# ndim: 3
# shape: (2, 2, 2)
# size: 8
# dtype: int64
