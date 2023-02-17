
from .Bjarne23 import Bjarne23


class Bjarne142(Bjarne23):
    def __init__(self):
        
        super().__init__()
        

        
        self.a = "p3kop3ko"
        
        
        self.b = "1337"
        
        
        
        self.d = "Pho3N1X"
        
        
        self.e = "8jaRn3"
        
        
        
        self.g = "5w49"
        
    
    def get_password(self):
        return "%s.%s.%s.%s.%s.%s" % (self.a, self.b, self.c, self.g, self.e, self.f)