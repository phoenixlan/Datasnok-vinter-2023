
from .Bjarne17 import Bjarne17


class Bjarne1326(Bjarne17):
    def __init__(self):
        
        super().__init__()
        

        
        self.a = "1337"
        
        
        self.b = "c00l5sh"
        
        
        self.c = "5w4G4d3Ll1c"
        
        
        self.d = "p3kop3ko"
        
        
        self.e = "IrhAh"
        
        
        self.f = "l3375P33k"
        
        
        self.g = "Pho3N1X"
        
    
    def get_password(self):
        return "%s.%s.%s.%s.%s.%s" % (self.a, self.b, self.c, self.g, self.e, self.f)