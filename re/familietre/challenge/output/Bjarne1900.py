
from .Bjarne4 import Bjarne4


class Bjarne1900(Bjarne4):
    def __init__(self):
        
        super().__init__()
        

        
        self.a = "p3kop3ko"
        
        
        self.b = "Pho3N1X"
        
        
        self.c = "5w49"
        
        
        
        self.e = "xR4Y"
        
        
        
    
    def get_password(self):
        return "%s.%s.%s.%s.%s.%s" % (self.a, self.b, self.c, self.g, self.e, self.f)