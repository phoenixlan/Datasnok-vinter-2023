
from .Bjarne1100 import Bjarne1100


class Bjarne1640(Bjarne1100):
    def __init__(self):
        
        super().__init__()
        

        
        self.a = "8jaRn3"
        
        
        
        
        
        self.e = "1337"
        
        
        self.f = "5w49"
        
        
        self.g = "IrhAh"
        
    
    def get_password(self):
        return "%s.%s.%s.%s.%s.%s" % (self.a, self.b, self.c, self.g, self.e, self.f)