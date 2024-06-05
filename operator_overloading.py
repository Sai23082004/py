# operator over loading 

class a:
    def __init__(self,a):
        self.a=a

    def __add__(self,other):
        return self.a+other.a
    def __gt__(self,other):
        if self.a>other.a:
            return True
        else:
            return False
    
obj1=a(10)
obj2=a(20)
print(obj1+obj2)
print(obj1>obj2)