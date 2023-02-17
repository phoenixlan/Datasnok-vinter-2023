
from .Bjarne1225 import Bjarne1225


class Bjarne1615(Bjarne1225):
    def __init__(self):
        
        super().__init__()
        

        
        
        
        
        self.d = "1337"
        
        
        
        
        self.g = "Pho3N1X"
        
    
    def get_password(self):
        return "%s.%s.%s.%s.%s.%s" % (self.a, self.b, self.c, self.g, self.e, self.f)