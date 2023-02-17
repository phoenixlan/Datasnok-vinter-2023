
from .Bjarne86 import Bjarne86


class Bjarne389(Bjarne86):
    def __init__(self):
        
        super().__init__()
        

        
        
        self.b = "1337"
        
        
        self.c = "1337"
        
        
        self.d = "p3kop3ko"
        
        
        self.e = "1337"
        
        
        
        self.g = "c00l5sh"
        
    
    def get_password(self):
        return "%s.%s.%s.%s.%s.%s" % (self.a, self.b, self.c, self.g, self.e, self.f)