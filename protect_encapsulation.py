#protecte in encapsulation 

class a:
    def __init__(self):
        self._a=10  # protected 
        self._b=20  # protected 

class b(a):
    def __init__(self):
        a.__init__(self)

    def show_data(self):
        print('a =',self._a)
        print('b =',self._b)

obj=b()
obj.show_data()