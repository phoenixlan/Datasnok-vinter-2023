
from .Bjarne785 import Bjarne785


class Bjarne1432(Bjarne785):
    def __init__(self):
        
        super().__init__()
        

        
        self.a = "1337"
        
        
        self.b = "1337"
        
        
        self.c = "c00l5sh"
        
        
        
        self.e = "l3375P33k"
        
        
        
        self.g = "xR4Y"
        
    
    def get_password(self):
        return "%s.%s.%s.%s.%s.%s" % (self.a, self.b, self.c, self.g, self.e, self.f)