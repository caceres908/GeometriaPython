import math
class Punto:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    

    def hallarDistancia(self, punto):
        d = math.sqrt(math.pow(self.x-punto.x,2)+math.pow(self.y - punto.y,2))
        return d


