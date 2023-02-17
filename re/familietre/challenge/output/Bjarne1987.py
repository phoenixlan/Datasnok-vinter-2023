
from .Bjarne1864 import Bjarne1864


class Bjarne1987(Bjarne1864):
    def __init__(self):
        
        super().__init__()
        

        
        
        
        
        self.d = "p3kop3ko"
        
        
        
        self.f = "xR4Y"
        
        
        self.g = "1337"
        
    
    def get_password(self):
        return "%s.%s.%s.%s.%s.%s" % (self.a, self.b, self.c, self.g, self.e, self.f)