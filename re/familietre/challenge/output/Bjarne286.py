
from .Bjarne32 import Bjarne32


class Bjarne286(Bjarne32):
    def __init__(self):
        
        super().__init__()
        

        
        
        self.b = "8jaRn3"
        
        
        
        self.d = "p3kop3ko"
        
        
        self.e = "xR4Y"
        
        
        self.f = "p3kop3ko"
        
        
    
    def get_password(self):
        return "%s.%s.%s.%s.%s.%s" % (self.a, self.b, self.c, self.g, self.e, self.f)