import unittest
from capicuas import es_capicua, generar_capicuas


class TestCapicuas(unittest.TestCase):

    # --- TESTS PARA es_capicua ---
    def test_es_capicua_true(self):
        self.assertTrue(es_capicua(121))
        self.assertTrue(es_capicua(1331))
        self.assertTrue(es_capicua(5))

    def test_es_capicua_false(self):
        self.assertFalse(es_capicua(123))
        self.assertFalse(es_capicua(987))
        self.assertFalse(es_capicua(120))

    # --- TESTS PARA generar_capicuas ---
    def test_generar_capicuas_rango_pequeño(self):
        resultado = generar_capicuas(1, 200)
        esperado = [1,2,3,4,5,6,7,8,9,11,22,33,44,55,66,77,88,99,101,111,121,131,141,151,161,171,181,191]
        self.assertEqual(resultado, esperado)

    def test_rango_sin_capicuas(self):
        resultado = generar_capicuas(123, 130)
        self.assertEqual(resultado, [])

    def test_limites_incluidos(self):
        resultado = generar_capicuas(121, 121)
        self.assertEqual(resultado, [121])


if __name__ == '__main__':
    unittest.main(verbosity=2)
