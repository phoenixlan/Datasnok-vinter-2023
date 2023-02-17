
from .Bjarne1195 import Bjarne1195


class Bjarne1815(Bjarne1195):
    def __init__(self):
        
        super().__init__()
        

        
        
        
        
        self.d = "5w49"
        
        
        self.e = "1337"
        
        
        
    
    def get_password(self):
        return "%s.%s.%s.%s.%s.%s" % (self.a, self.b, self.c, self.g, self.e, self.f)