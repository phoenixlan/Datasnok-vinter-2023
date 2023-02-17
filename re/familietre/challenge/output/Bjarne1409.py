
from .Bjarne1258 import Bjarne1258


class Bjarne1409(Bjarne1258):
    def __init__(self):
        
        super().__init__()
        

        
        self.a = "xbg"
        
        
        self.b = "1337"
        
        
        
        
        
        
    
    def get_password(self):
        return "%s.%s.%s.%s.%s.%s" % (self.a, self.b, self.c, self.g, self.e, self.f)