
from .Bjarne717 import Bjarne717


class Bjarne1602(Bjarne717):
    def __init__(self):
        
        super().__init__()
        

        
        
        
        self.c = "1337"
        
        
        
        
        
        self.g = "5w49"
        
    
    def get_password(self):
        return "%s.%s.%s.%s.%s.%s" % (self.a, self.b, self.c, self.g, self.e, self.f)