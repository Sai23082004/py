#Arithmetic Operators
a = 10
b = 5
print("Addition:", a + b) 
print("Subtraction:", a - b) 
print("Multiplication:", a * b)
print("Division:", a / b) 
print("Modulus:", a % b) 
print("Exponentiation:", a ** b) 
print("Floor Division:", a // b)
#Relational Operators
x = 10
y = 5
print("Equal:", x == y) 
print("Not Equal:", x != y) 
print("Greater than:", x > y) 
print("Less than:", x < y) 
print("Greater than or equal to:", x >= y) 
print("Less than or equal to:", x <= y)

# Assignment Operators
z = 10
z += 5 
print("z += 5:", z)
z -= 3 
print("z -= 3:", z)
z *= 2 
print("z *= 2:", z)
z /= 4 
print("z /= 4:", z)
z %= 2 
print("z %= 2:", z)
z **= 3 
print("z **= 3:", z)
z //= 2
print("z //= 2:", z)
# Logical Operators
a = True
b = False
print("Logical AND:", a and b) 
print("Logical OR:", a or b) 
print("Logical NOT:", not a) 
# Bitwise Operators
a = 10 # 1010 in binary
b = 4 # 0100 in binary
print("Bitwise AND:", a & b) 
print("Bitwise OR:", a | b) 
print("Bitwise XOR:", a ^ b) 
print("Bitwise NOT:", ~a) 
print("Bitwise LEFT SHIFT:", a << 2) 
print("Bitwise RIGHT SHIFT:", a >> 2)
# Ternary Operator
a = 10
b = 20
max_value = a if a > b else b
print("Ternary Operator Result (max_value):", max_value)

# Membership Operators
my_list = [1, 2, 3, 4, 5]
print("Is 3 in the list?", 3 in my_list) 
print("Is 6 not in the list?", 6 not in my_list)
# Identity Operators
x = 5
y = 5
z = [1, 2, 3]
w = [1, 2, 3]
print("x is y:", x is y) 
print("z is w:", z is w) 
print("z is not w:", z is not w)

# OUTPUT:
# Addition: 15
# Subtraction: 5
# Multiplication: 50
# Division: 2.0
# Modulus: 0
# Exponentiation: 100000
# Floor Division: 2
# Equal: False
# Not Equal: True
# Greater than: True
# Less than: False
# Greater than or equal to: True
# Less than or equal to: False
# z += 5: 15
# z -= 3: 12
# z *= 2: 24
# z /= 4: 6.0
# z %= 2: 0.0
# z **= 3: 0.0
# z //= 2: 0.0
# Logical AND: False
# Logical OR: True
# Logical NOT: False
# Bitwise AND: 0
# Bitwise OR: 14
# Bitwise XOR: 14
# Bitwise NOT: -11
# Bitwise LEFT SHIFT: 40
# Bitwise RIGHT SHIFT: 2
# Ternary Operator Result (max_value): 20
# Is 3 in the list? True
# Is 6 not in the list? True
# x is y: True
# z is w: False
# z is not w: True
