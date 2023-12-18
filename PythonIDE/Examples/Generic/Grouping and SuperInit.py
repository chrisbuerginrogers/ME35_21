class Elements():
    def __init__(self, a,b):
        print(a,b)
    
class Div(Elements):
    def __init__(self, a):
        super().__init__(a,2)
        pass
    
    def value(self):
        return 2
    
class Button(Elements):
    def __init__(self,c):
        super().__init__(c,5)
        pass
    
    def value(self):
        return 5

class Group():
    def __init__(self, *args):
        self.value = 0
        for v in args:
            self.value += v.value()
        print(self.value)
        
 
class Cluster():
    def __init__(self, **args):
        self.value = 0
        for k,v in args.items():
            self.value += v.value()
            print(k, v.value())
        print(self.value)

        
div = Div('a')
btn = Button('b')

group = Group(div,btn)
cluster = Cluster(div = div,btn = btn)
            
