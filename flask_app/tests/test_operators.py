import unittest
from flask_app.operators import add, subtract, multiply, divide

class TestOperators(unittest.TestCase):
    """
    Classe de tests pour les fonctions d'opérations arithmétiques.
    Vérifie le bon fonctionnement de add, subtract, multiply et divide, 
    ainsi que la gestion des erreurs (division par zéro).
    """
    def test_add(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 5), 4)
        self.assertEqual(add(0, 0), 0)

    def test_subtract(self):
        self.assertEqual(subtract(5, 2), 3)
        self.assertEqual(subtract(2, 5), -3)
        self.assertEqual(subtract(0, 0), 0)

    def test_multiply(self):
        self.assertEqual(multiply(3, 4), 12)
        self.assertEqual(multiply(-2, 5), -10)
        self.assertEqual(multiply(0, 100), 0)

    def test_divide(self):
        self.assertEqual(divide(10, 2), 5.0)
        self.assertEqual(divide(9, 4), 2.25)
        self.assertEqual(divide(-9, 4), -2.25)

        with self.assertRaises(ZeroDivisionError):
            divide(5, 0)

if __name__ == '__main__':
    unittest.main()
