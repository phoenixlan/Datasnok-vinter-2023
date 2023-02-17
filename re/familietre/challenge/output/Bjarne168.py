
from .Bjarne9 import Bjarne9


class Bjarne168(Bjarne9):
    def __init__(self):
        
        super().__init__()
        

        
        self.a = "1337"
        
        
        self.b = "l3375P33k"
        
        
        self.c = "Pho3N1X"
        
        
        self.d = "xR4Y"
        
        
        
        self.f = "5w49"
        
        
        self.g = "l3375P33k"
        
    
    def get_password(self):
        return "%s.%s.%s.%s.%s.%s" % (self.a, self.b, self.c, self.g, self.e, self.f)