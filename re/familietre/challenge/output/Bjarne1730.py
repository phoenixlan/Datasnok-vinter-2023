
from .Bjarne1405 import Bjarne1405


class Bjarne1730(Bjarne1405):
    def __init__(self):
        
        super().__init__()
        

        
        
        
        
        self.d = "1337"
        
        
        
        self.f = "p3kop3ko"
        
        
        self.g = "xR4Y"
        
    
    def get_password(self):
        return "%s.%s.%s.%s.%s.%s" % (self.a, self.b, self.c, self.g, self.e, self.f)