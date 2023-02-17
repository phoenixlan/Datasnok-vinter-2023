
from .Bjarne1793 import Bjarne1793


class Bjarne1936(Bjarne1793):
    def __init__(self):
        
        super().__init__()
        

        
        
        
        
        
        
        self.f = "xbg"
        
        
    
    def get_password(self):
        return "%s.%s.%s.%s.%s.%s" % (self.a, self.b, self.c, self.g, self.e, self.f)