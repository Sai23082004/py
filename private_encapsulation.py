'''
encapsulation means combining methods and artibutes in the same class 
mainly protection purpose 
1) public 
2) private 
only class methods and inside the class 
3) protected 
in clsses and subclasses 

'''
class a:
    def __init__(self,a,b):
        self.__a=a #private 
        self.__b=b  #private

    def show_data(self):
        print('a =',self.__a)
        print('b =',self.__b)

obj1= a(10,20)
#print(obj1.a)   ----error will be occured 
obj1.show_data()