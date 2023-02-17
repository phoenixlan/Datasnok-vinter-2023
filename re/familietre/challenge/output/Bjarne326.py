
from .Bjarne261 import Bjarne261


class Bjarne326(Bjarne261):
    def __init__(self):
        
        super().__init__()
        

        
        self.a = "p3kop3ko"
        
        
        self.b = "l3375P33k"
        
        
        
        self.d = "1337"
        
        
        self.e = "1337"
        
        
        self.f = "p3kop3ko"
        
        
        self.g = "l3375P33k"
        
    
    def get_password(self):
        return "%s.%s.%s.%s.%s.%s" % (self.a, self.b, self.c, self.g, self.e, self.f)