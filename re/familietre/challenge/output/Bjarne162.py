
from .Bjarne16 import Bjarne16


class Bjarne162(Bjarne16):
    def __init__(self):
        
        super().__init__()
        

        
        self.a = "1337"
        
        
        self.b = "c00l5sh"
        
        
        self.c = "IrhAh"
        
        
        
        self.e = "p3kop3ko"
        
        
        self.f = "xbg"
        
        
        self.g = "5w4G4d3Ll1c"
        
    
    def get_password(self):
        return "%s.%s.%s.%s.%s.%s" % (self.a, self.b, self.c, self.g, self.e, self.f)