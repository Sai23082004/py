'''
polymorphism ---- means many ways 
1) method over loading 
2) method over riding  
'''

def add(a,b,c=0,d=0,e=0):
    add=a+b+c+d+e
    print('answer is :- ',add)

add(2,3)
add(2,3,4)
add(4,3,2,1)
add(1,2,3,4,5)
# another example for method over loading 
l=[1,2,3,4,4]
s='hello world!'
print(len(l))
print(len(s))