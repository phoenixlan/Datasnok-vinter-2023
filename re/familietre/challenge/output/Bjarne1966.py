
from .Bjarne938 import Bjarne938


class Bjarne1966(Bjarne938):
    def __init__(self):
        
        super().__init__()
        

        
        self.a = "5w49"
        
        
        self.b = "1337"
        
        
        self.c = "5w49"
        
        
        
        
        self.f = "Pho3N1X"
        
        
        self.g = "xbg"
        
    
    def get_password(self):
        return "%s.%s.%s.%s.%s.%s" % (self.a, self.b, self.c, self.g, self.e, self.f)