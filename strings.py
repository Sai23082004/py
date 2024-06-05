v1='strings in py '
# printg string 
for characters in v1:
    print(characters)

# print assci valuees of characters 
for characters in v1:
    print(ord(characters))
print()
#print ascii value to character 
print(chr(97))
#captial letters to small letter 
v2='HELLO SAIKIRAN'
print(v2.lower())# small characters function 
print(v1.upper())# upper characters function

# add two strings 
res=print(v1+v2)

#comparing strings 
if(v1==v2):
    print('equal')
else:
    print('not equal')
# string slicing 
print(v1[0:3])
l=['how','are,you']
la='how is it going'
#spliting a string 
print(list(la.split(' ')))
# joining method 
result_str=' '.join(l)
print(result_str)
#conversion
print(type(l))
t=tuple(l)
print(type(t))
# f strings 
v=10
j=30
k=40
print(f'a:{v},b:{j},c:{k}')
 