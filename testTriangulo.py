import unittest
from Punto import Punto
from Triangulo import Triangulo

class TestTriangulo(unittest.TestCase):
    def test_hallarArea(self):
        puntos = [Punto(0,0), Punto(1,0), Punto(0.5,1)]
        t = Triangulo(puntos)        
        area = t.hallarArea()
        self.assertEqual(area,0.5)
    
    def test_hallarPerimetro(self):
        puntos = [Punto(0,0), Punto(3,0), Punto(0,4)]
        t = Triangulo(puntos)
        perimetro = t.hallarPerimetro()
        self.assertEqual(perimetro,12)
        

if __name__ == "__main__":
    unittest.main()