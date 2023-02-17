
from .Bjarne84 import Bjarne84


class Bjarne214(Bjarne84):
    def __init__(self):
        
        super().__init__()
        

        
        self.a = "1337"
        
        
        
        self.c = "k3wL_83An5"
        
        
        
        self.e = "xbg"
        
        
        
        self.g = "c00l5sh"
        
    
    def get_password(self):
        return "%s.%s.%s.%s.%s.%s" % (self.a, self.b, self.c, self.g, self.e, self.f)