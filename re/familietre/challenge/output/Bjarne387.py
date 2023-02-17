
from .Bjarne134 import Bjarne134


class Bjarne387(Bjarne134):
    def __init__(self):
        
        super().__init__()
        

        
        self.a = "1337"
        
        
        
        self.c = "xR4Y"
        
        
        
        self.e = "5w49"
        
        
        
        self.g = "c00l5sh"
        
    
    def get_password(self):
        return "%s.%s.%s.%s.%s.%s" % (self.a, self.b, self.c, self.g, self.e, self.f)