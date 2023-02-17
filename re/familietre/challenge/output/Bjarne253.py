
from .Bjarne38 import Bjarne38


class Bjarne253(Bjarne38):
    def __init__(self):
        
        super().__init__()
        

        
        
        
        self.c = "1337"
        
        
        
        self.e = "Pho3N1X"
        
        
        
        self.g = "IrhAh"
        
    
    def get_password(self):
        return "%s.%s.%s.%s.%s.%s" % (self.a, self.b, self.c, self.g, self.e, self.f)