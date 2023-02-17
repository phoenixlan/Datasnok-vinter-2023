
from .Bjarne74 import Bjarne74


class Bjarne120(Bjarne74):
    def __init__(self):
        
        super().__init__()
        

        
        self.a = "1337"
        
        
        
        self.c = "k3wL_83An5"
        
        
        
        self.e = "8jaRn3"
        
        
        self.f = "5w4G4d3Ll1c"
        
        
    
    def get_password(self):
        return "%s.%s.%s.%s.%s.%s" % (self.a, self.b, self.c, self.g, self.e, self.f)