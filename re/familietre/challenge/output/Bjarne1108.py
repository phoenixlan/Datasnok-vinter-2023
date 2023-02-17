
from .Bjarne512 import Bjarne512


class Bjarne1108(Bjarne512):
    def __init__(self):
        
        super().__init__()
        

        
        self.a = "Pho3N1X"
        
        
        self.b = "1337"
        
        
        self.c = "5w49"
        
        
        self.d = "5w49"
        
        
        self.e = "Pho3N1X"
        
        
        self.f = "xR4Y"
        
        
    
    def get_password(self):
        return "%s.%s.%s.%s.%s.%s" % (self.a, self.b, self.c, self.g, self.e, self.f)