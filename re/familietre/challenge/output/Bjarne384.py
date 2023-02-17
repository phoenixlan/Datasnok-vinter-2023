
from .Bjarne75 import Bjarne75


class Bjarne384(Bjarne75):
    def __init__(self):
        
        super().__init__()
        

        
        self.a = "5w4G4d3Ll1c"
        
        
        self.b = "5w4G4d3Ll1c"
        
        
        self.c = "5w49"
        
        
        
        
        
        self.g = "1337"
        
    
    def get_password(self):
        return "%s.%s.%s.%s.%s.%s" % (self.a, self.b, self.c, self.g, self.e, self.f)