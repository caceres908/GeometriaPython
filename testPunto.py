import unittest
from Punto import Punto

class TestPunto(unittest.TestCase):
    def test_hallarDistancia(self):
        p1 = Punto(-1, 0)
        p2 = Punto(0, 1)
        f = p1.hallarDistancia(p2)
        self.assertEqual(f, 1.4142135623730951)
        

if __name__ == "__main__":
    unittest.main()
