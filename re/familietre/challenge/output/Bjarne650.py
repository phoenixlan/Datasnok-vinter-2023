
from .Bjarne256 import Bjarne256


class Bjarne650(Bjarne256):
    def __init__(self):
        
        super().__init__()
        

        
        self.a = "5w49"
        
        
        self.b = "p3kop3ko"
        
        
        
        self.d = "5w4G4d3Ll1c"
        
        
        
        self.f = "Pho3N1X"
        
        
        self.g = "xR4Y"
        
    
    def get_password(self):
        return "%s.%s.%s.%s.%s.%s" % (self.a, self.b, self.c, self.g, self.e, self.f)