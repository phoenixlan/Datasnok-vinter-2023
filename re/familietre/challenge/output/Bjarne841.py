
from .Bjarne384 import Bjarne384


class Bjarne841(Bjarne384):
    def __init__(self):
        
        super().__init__()
        

        
        self.a = "1337"
        
        
        self.b = "1337"
        
        
        
        self.d = "8jaRn3"
        
        
        self.e = "1337"
        
        
        
        self.g = "xbg"
        
    
    def get_password(self):
        return "%s.%s.%s.%s.%s.%s" % (self.a, self.b, self.c, self.g, self.e, self.f)