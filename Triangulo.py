import math
class Triangulo():
    def __init__(self, arista):
        self.arista = arista
        self.lado1 = arista[0].hallarDistancia(arista[1])
        self.lado2 = arista[0].hallarDistancia(arista[2])
        self.lado3 = arista[1].hallarDistancia(arista[2])
    

    def hallarArea(self):
        s = (self.hallarPerimetro()/2)
        altura = (2/self.lado1) * math.sqrt(s*(s-self.lado1)*(s-self.lado2)*(s-self.lado3))
        area = (altura*self.lado1)/2
        return area

    def hallarPerimetro(self):
        perimetro = self.lado1 + self.lado2 + self.lado3
        return perimetro 