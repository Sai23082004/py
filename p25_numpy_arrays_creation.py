import numpy as np

# Creating a 1-dimensional array
array_1d = np.array([1, 2, 3, 4, 5])
print("1D Array:", array_1d)

# Creating a 2-dimensional array
array_2d = np.array([[1, 2, 3],
                     [4, 5, 6],
                     [7, 8, 9]])
print("\n2D Array:\n", array_2d)

# Creating a 3-dimensional array
array_3d = np.array([[[1, 2], [3, 4]],
                     [[5, 6], [7, 8]],
                     [[9, 10], [11, 12]]])
print("\n3D Array:\n", array_3d)
# OUTPUT:
# 1D Array: [1 2 3 4 5]

# 2D Array:
#  [[1 2 3]
#  [4 5 6]
#  [7 8 9]]

# 3D Array:
#  [[[ 1  2]
#   [ 3  4]]

#  [[ 5  6]
#   [ 7  8]]

#  [[ 9 10]
#   [11 12]]]
