
from .Bjarne14 import Bjarne14


class Bjarne1851(Bjarne14):
    def __init__(self):
        
        super().__init__()
        

        
        self.a = "8jaRn3"
        
        
        self.b = "1337"
        
        
        
        self.d = "xbg"
        
        
        self.e = "8jaRn3"
        
        
        self.f = "l3375P33k"
        
        
        self.g = "l3375P33k"
        
    
    def get_password(self):
        return "%s.%s.%s.%s.%s.%s" % (self.a, self.b, self.c, self.g, self.e, self.f)