
from .Bjarne1899 import Bjarne1899


class Bjarne1909(Bjarne1899):
    def __init__(self):
        
        super().__init__()
        

        
        self.a = "xbg"
        
        
        self.b = "1337"
        
        
        self.c = "IrhAh"
        
        
        
        self.e = "l3375P33k"
        
        
        
        self.g = "5w49"
        
    
    def get_password(self):
        return "%s.%s.%s.%s.%s.%s" % (self.a, self.b, self.c, self.g, self.e, self.f)