
from .Bjarne91 import Bjarne91


class Bjarne1871(Bjarne91):
    def __init__(self):
        
        super().__init__()
        

        
        self.a = "1337"
        
        
        self.b = "8jaRn3"
        
        
        
        self.d = "IrhAh"
        
        
        self.e = "1337"
        
        
        self.f = "k3wL_83An5"
        
        
        self.g = "k3wL_83An5"
        
    
    def get_password(self):
        return "%s.%s.%s.%s.%s.%s" % (self.a, self.b, self.c, self.g, self.e, self.f)