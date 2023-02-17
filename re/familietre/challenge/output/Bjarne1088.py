
from .Bjarne20 import Bjarne20


class Bjarne1088(Bjarne20):
    def __init__(self):
        
        super().__init__()
        

        
        self.a = "p3kop3ko"
        
        
        self.b = "c00l5sh"
        
        
        self.c = "xbg"
        
        
        
        self.e = "1337"
        
        
        self.f = "IrhAh"
        
        
        self.g = "Pho3N1X"
        
    
    def get_password(self):
        return "%s.%s.%s.%s.%s.%s" % (self.a, self.b, self.c, self.g, self.e, self.f)