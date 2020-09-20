import unittest
from Punto import Punto
from Circulo import Circulo

class TestCirculo(unittest.TestCase):
    def test_hallarArea(self):
        c = Circulo(4,Punto(1,2))
        area = c.hallarArea()
        self.assertEqual(area,50.26548245743669)

    def test_hallarPerimetro(self):
        c = Circulo(4,Punto(1,2))
        perimetro = c.hallarPerimetro()
        self.assertEqual(perimetro,25.132741228718345)

    def test_estaEnElCirculo(self):
        c = Circulo(4,Punto(1,2))
        p1 = Punto(-1,0)
        f = c.estaEnElCirculo(p1)
        self.assertEqual(f,True)
       
        

if __name__ == "__main__":
    unittest.main()
