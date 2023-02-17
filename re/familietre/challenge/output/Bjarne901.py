
from .Bjarne100 import Bjarne100


class Bjarne901(Bjarne100):
    def __init__(self):
        
        super().__init__()
        

        
        
        self.b = "1337"
        
        
        self.c = "l3375P33k"
        
        
        self.d = "p3kop3ko"
        
        
        self.e = "p3kop3ko"
        
        
        self.f = "p3kop3ko"
        
        
        self.g = "1337"
        
    
    def get_password(self):
        return "%s.%s.%s.%s.%s.%s" % (self.a, self.b, self.c, self.g, self.e, self.f)