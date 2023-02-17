
from .Bjarne51 import Bjarne51


class Bjarne1942(Bjarne51):
    def __init__(self):
        
        super().__init__()
        

        
        self.a = "p3kop3ko"
        
        
        self.b = "p3kop3ko"
        
        
        self.c = "IrhAh"
        
        
        
        self.e = "p3kop3ko"
        
        
        self.f = "c00l5sh"
        
        
        self.g = "1337"
        
    
    def get_password(self):
        return "%s.%s.%s.%s.%s.%s" % (self.a, self.b, self.c, self.g, self.e, self.f)