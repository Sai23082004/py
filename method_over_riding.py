class parent:
    def __init__(self):
        pass
    def height(self):
        print('height =',5.7)
    def edjucation(self):
        print('edjucation =','degree')
    def surname(self):
        print('xyz')

class son(parent):
    def __init__(self):
        parent.__init__(self)
    def height(self):
        print('height',6.1)
    def edjucation(self):
        print('edjucation','engineering')


father=parent()
son=son()


son.height()
son.edjucation()
son.surname()
