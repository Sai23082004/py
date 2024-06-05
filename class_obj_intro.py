class student:
    def __init__(self,id,age,name):
        self.id=id
        self.age=age
        self.name=name

    def print_details(self):
        print(self.id,self.age,self.name)

v1=student(1,22,'sai')
v2=student(2,23,'dharani')

print(v1.id,v1.age,v1.name)
print(v2.id,v2.age,v2.name)
# using function to print details 
print('after using function-------\n')
v1.print_details()
v2.print_details()