
from .Bjarne128 import Bjarne128


class Bjarne1381(Bjarne128):
    def __init__(self):
        
        super().__init__()
        

        
        
        self.b = "1337"
        
        
        
        
        self.e = "5w49"
        
        
        self.f = "xR4Y"
        
        
        self.g = "1337"
        
    
    def get_password(self):
        return "%s.%s.%s.%s.%s.%s" % (self.a, self.b, self.c, self.g, self.e, self.f)