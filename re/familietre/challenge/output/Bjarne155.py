
from .Bjarne67 import Bjarne67


class Bjarne155(Bjarne67):
    def __init__(self):
        
        super().__init__()
        

        
        self.a = "1337"
        
        
        
        
        self.d = "8jaRn3"
        
        
        
        self.f = "5w49"
        
        
    
    def get_password(self):
        return "%s.%s.%s.%s.%s.%s" % (self.a, self.b, self.c, self.g, self.e, self.f)