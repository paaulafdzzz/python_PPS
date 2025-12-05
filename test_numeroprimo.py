import unittest
from numeroprimo import es_primo

class TestPrimo(unittest.TestCase):

    def test_primo_valido(self):
        self.assertTrue(es_primo(7))     # 7 es primo

    def test_no_primo(self):
        self.assertFalse(es_primo(8))    # 8 no es primo

    def test_numero_1(self):
        self.assertFalse(es_primo(1))    # 1 NO es primo

    def test_numero_0(self):
        self.assertFalse(es_primo(0))    # 0 NO es primo

    def test_numero_negativo(self):
        self.assertFalse(es_primo(-5))   # negativos tampoco

    def test_primo_grande(self):
        self.assertTrue(es_primo(97))    # 97 también es primo

if __name__ == '__main__':
    unittest.main(verbosity=2)
