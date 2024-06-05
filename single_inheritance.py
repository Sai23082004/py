'''
inheritance concept 
types of ineritance
1) single level inheritance
2) multi level ingeritance 
3_multiple inheritance
4)heirarical inheritance
5)hybrid inheritance 
'''
class a:
    def __init__(self,a_value):
        self.a_value=a_value

    def print_a(self):
        print('a value=',self.a_value)

class b(a):
    def __init__(self,a_value,b_value):
        a.__init__(self,a_value)
        self.b_value=b_value

    def print_b(self):
        print('b value=',self.b_value)

obj1=b(10,20)
obj1.print_a()