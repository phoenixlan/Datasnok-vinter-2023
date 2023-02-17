
from .Bjarne64 import Bjarne64


class Bjarne195(Bjarne64):
    def __init__(self):
        
        super().__init__()
        

        
        
        
        
        self.d = "8jaRn3"
        
        
        self.e = "IrhAh"
        
        
        
        self.g = "xR4Y"
        
    
    def get_password(self):
        return "%s.%s.%s.%s.%s.%s" % (self.a, self.b, self.c, self.g, self.e, self.f)