class Rectangulo:
    def __init__(self, arista):
        self.arista = arista
        if arista[0].hallarDistancia(arista[1]) == arista[2].hallarDistancia(arista[3]):
            if arista[0].hallarDistancia(arista[2]) == arista[1].hallarDistancia(arista[3]):
                self.lado1 = arista[0].hallarDistancia(arista[1])
                self.lado2 = arista[0].hallarDistancia(arista[2])
            elif arista[0].hallarDistancia(arista[3]) == arista[1].hallarDistancia(arista[2]):
                self.lado1 = arista[0].hallarDistancia(arista[1])
                self.lado2 = arista[0].hallarDistancia(arista[3])
        elif arista[0].hallarDistancia(arista[2]) == arista[1].hallarDistancia(arista[3]):
             if arista[0].hallarDistancia(arista[3]) == arista[2].hallarDistancia(arista[1]):
                 self.lado1 = arista[0].hallarDistancia(arista[2])
                 self.lado2 = arista[0].hallarDistancia(arista[3])

    def hallarArea(self):
        area = self.lado1 * self.lado2
        return area

    def hallarPerimetro(self):
        perimetro = (self.lado1*2) + (self.lado2*2)
        return perimetro


          