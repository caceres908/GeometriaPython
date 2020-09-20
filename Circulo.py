import math
class Circulo:
    def __init__(self, radio, centro):
        self.radio = radio
        self.centro = centro

    def hallarArea(self):
        area = math.pi * math.pow(self.radio, 2)
        return area

    def hallarPerimetro(self):
        perimetro = 2 * math.pi * self.radio
        return perimetro

    def estaEnElCirculo(self, punto):
        if self.centro.hallarDistancia(punto) <= self.radio:
            return True
        else:
            return False
