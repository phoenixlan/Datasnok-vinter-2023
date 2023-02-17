
from .Bjarne144 import Bjarne144


class Bjarne1983(Bjarne144):
    def __init__(self):
        
        super().__init__()
        

        
        self.a = "p3kop3ko"
        
        
        self.b = "1337"
        
        
        self.c = "xR4Y"
        
        
        self.d = "k3wL_83An5"
        
        
        self.e = "IrhAh"
        
        
        self.f = "p3kop3ko"
        
        
        self.g = "1337"
        
    
    def get_password(self):
        return "%s.%s.%s.%s.%s.%s" % (self.a, self.b, self.c, self.g, self.e, self.f)