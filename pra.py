class a:
    def __init__(self,a):
        self.a_v=a
    def print_a(self):
        print("a vlaue =",self.a_v)

class b(a):
    def __init__(self,a_v,b):
        a.__init__(self,a_v)
        self.b=b
    def print_b(self):
        print('b value =',self.b)

obj1=b(20,30)
obj1.print_a()