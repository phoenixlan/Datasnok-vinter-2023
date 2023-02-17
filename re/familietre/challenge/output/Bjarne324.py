
from .Bjarne96 import Bjarne96


class Bjarne324(Bjarne96):
    def __init__(self):
        
        super().__init__()
        

        
        
        
        self.c = "1337"
        
        
        self.d = "l3375P33k"
        
        
        
        
        self.g = "xR4Y"
        
    
    def get_password(self):
        return "%s.%s.%s.%s.%s.%s" % (self.a, self.b, self.c, self.g, self.e, self.f)