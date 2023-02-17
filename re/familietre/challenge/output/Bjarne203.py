
from .Bjarne91 import Bjarne91


class Bjarne203(Bjarne91):
    def __init__(self):
        
        super().__init__()
        

        
        self.a = "1337"
        
        
        self.b = "xR4Y"
        
        
        self.c = "IrhAh"
        
        
        
        self.e = "5w4G4d3Ll1c"
        
        
        
        self.g = "xbg"
        
    
    def get_password(self):
        return "%s.%s.%s.%s.%s.%s" % (self.a, self.b, self.c, self.g, self.e, self.f)