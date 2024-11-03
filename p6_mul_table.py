number = int(input("Enter a number to print its multiplication table: "))
upto = int(input("Enter the range for the multiplication table (default is 10): "))
print ("The Multiplication Table of: ", number)    
for count in range(1, upto+1):      
   print (number, 'x', count, '=', number * count)    
        
# OUTPUT:
# Enter a number to print its multiplication table: 5
# Enter the range for the multiplication table (default is 10): 5
# The Multiplication Table of:  5
# 5 x 1 = 5
# 5 x 2 = 10
# 5 x 3 = 15
# 5	x 4 = 20
# 5 x 5 = 25
