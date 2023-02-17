
from .Bjarne331 import Bjarne331


class Bjarne1620(Bjarne331):
    def __init__(self):
        
        super().__init__()
        

        
        self.a = "xR4Y"
        
        
        
        
        self.d = "5w49"
        
        
        
        
        self.g = "1337"
        
    
    def get_password(self):
        return "%s.%s.%s.%s.%s.%s" % (self.a, self.b, self.c, self.g, self.e, self.f)