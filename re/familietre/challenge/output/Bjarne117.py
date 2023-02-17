
from .Bjarne80 import Bjarne80


class Bjarne117(Bjarne80):
    def __init__(self):
        
        super().__init__()
        

        
        self.a = "1337"
        
        
        self.b = "1337"
        
        
        
        
        self.e = "IrhAh"
        
        
        self.f = "IrhAh"
        
        
    
    def get_password(self):
        return "%s.%s.%s.%s.%s.%s" % (self.a, self.b, self.c, self.g, self.e, self.f)