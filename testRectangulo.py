import unittest
from Punto import Punto
from Rectangulo import Rectangulo

class TestRectangulo(unittest.TestCase):
    def test_hallarArea(self):
        puntos = [Punto(1,0), Punto(1,1), Punto(3,0), Punto(3,1)]
        r = Rectangulo(puntos)
        area = r.hallarArea()
        self.assertEqual(area,2)

    def test_hallarPerimetro(self):
        puntos = [Punto(1,0), Punto(1,1), Punto(3,0), Punto(3,1)]
        r = Rectangulo(puntos)
        perimetro = r.hallarPerimetro()
        self.assertEqual(perimetro,6)
               

if __name__ == "__main__":
    unittest.main()