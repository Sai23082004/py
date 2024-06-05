class a:
    def __init__(self):
        self.a=10

class b:
    def __init__(self):
        self.a=100

class c(a,b):
    def __init__(self):
        a.__init__(self)
        b.__init__(self)
        self.a=1

obj=c()
print(obj.a)        