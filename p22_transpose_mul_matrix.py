def matrix_addition(A, B):
    result = [[A[i][j] + B[i][j] for j in range(len(A[0]))] for i in range(len(A))]
    return result

def matrix_transpose(A):
    result = [[A[j][i] for j in range(len(A))] for i in range(len(A[0]))]
    return result

def matrix_multiplication(A, B):
    result = [[sum(A[i][k] * B[k][j] for k in range(len(B))) for j in range(len(B[0]))] for i in range(len(A))]
    return result

def print_matrix(matrix, name):
    print(f"{name}:")
    for row in matrix:
        print(row)
    print()  # Add a blank line for better readability

# Matrices
A = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]

B = [[4, 5, 6],
     [3, 4, 5],
     [2, 3, 4]]

# Perform and print all operations
addition_result = matrix_addition(A, B)
transpose_result = matrix_transpose(A)
multiplication_result = matrix_multiplication(A, B)

# Print results
print_matrix(addition_result, "Matrix Addition Result")
print_matrix(transpose_result, "Matrix Transpose Result (of A)")
print_matrix(multiplication_result, "Matrix Multiplication Result")
# output:
# Matrix Addition Result:
# [5, 7, 9]
# [7, 9, 11]
# [9, 11, 13]

# Matrix Transpose Result (of A):
# [1, 4, 7]
# [2, 5, 8]
# [3, 6, 9]

# Matrix Multiplication Result:
# [16, 22, 28]
# [43, 58, 73]
# [70, 94, 118]
