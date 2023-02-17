
from .Bjarne43 import Bjarne43


class Bjarne652(Bjarne43):
    def __init__(self):
        
        super().__init__()
        

        
        self.a = "1337"
        
        
        self.b = "p3kop3ko"
        
        
        self.c = "c00l5sh"
        
        
        
        
        
        self.g = "k3wL_83An5"
        
    
    def get_password(self):
        return "%s.%s.%s.%s.%s.%s" % (self.a, self.b, self.c, self.g, self.e, self.f)