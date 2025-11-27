import unittest
from ejercicio1 import es_bisiesto

class TestBisiesto(unittest.TestCase):

    def test_bisiesto_valido(self):
        self.assertTrue(es_bisiesto(2024))  # debe ser bisiesto

    def test_no_bisiesto(self):
        self.assertFalse(es_bisiesto(2023))  # no es bisiesto

    def test_secular_no_bisiesto(self):
        self.assertFalse(es_bisiesto(1900))  # divisible entre 100 pero no entre 400

    def test_secular_bisiesto(self):
        self.assertTrue(es_bisiesto(2000))   # divisible entre 400 sí es bisiesto

if __name__ == '__main__':
    unittest.main(verbosity=2)
