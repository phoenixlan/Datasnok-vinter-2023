
from .Bjarne5 import Bjarne5


class Bjarne472(Bjarne5):
    def __init__(self):
        
        super().__init__()
        

        
        
        
        
        
        
        self.f = "p3kop3ko"
        
        
    
    def get_password(self):
        return "%s.%s.%s.%s.%s.%s" % (self.a, self.b, self.c, self.g, self.e, self.f)