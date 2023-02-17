
from .Bjarne42 import Bjarne42


class Bjarne631(Bjarne42):
    def __init__(self):
        
        super().__init__()
        

        
        self.a = "1337"
        
        
        
        self.c = "c00l5sh"
        
        
        
        self.e = "5w49"
        
        
        self.f = "IrhAh"
        
        
        self.g = "Pho3N1X"
        
    
    def get_password(self):
        return "%s.%s.%s.%s.%s.%s" % (self.a, self.b, self.c, self.g, self.e, self.f)