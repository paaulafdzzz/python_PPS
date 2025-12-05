import unittest
from fibonacci import fibonacci   # importa tu función (cambia ejercicio por el nombre de tu archivo)

class TestFibonacci(unittest.TestCase):

    def test_0_terminos(self):
        self.assertEqual(fibonacci(0), [])

    def test_1_termino(self):
        self.assertEqual(fibonacci(1), [1])

    def test_2_terminos(self):
        self.assertEqual(fibonacci(2), [1, 1])

    def test_5_terminos(self):
        self.assertEqual(fibonacci(5), [1, 1, 2, 3, 5])

    def test_10_terminos(self):
        self.assertEqual(fibonacci(10),
                         [1,1,2,3,5,8,13,21,34,55])

    def test_numero_negativo(self):
        # Depende de tu criterio: aquí asumimos que debe devolver lista vacía
        self.assertEqual(fibonacci(-5), [])

if __name__ == '__main__':
    unittest.main(verbosity=2)
