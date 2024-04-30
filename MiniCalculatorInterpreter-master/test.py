import unittest
from my_math_functions import addition, soustraction, multiplication, division

class TestMathFunctions(unittest.TestCase):

    def test_addition(self):
        self.assertEqual(addition(3, 5), 8)
        self.assertEqual(addition(-3, 5), 2)
        self.assertEqual(addition(0, 0), 0)

    def test_soustraction(self):
        self.assertEqual(soustraction(10, 4), 6)
        self.assertEqual(soustraction(4, 10), -6)
        self.assertEqual(soustraction(0, 0), 0)

    def test_multiplication(self):
        self.assertEqual(multiplication(2, 7), 14)
        self.assertEqual(multiplication(-2, 7), -14)
        self.assertEqual(multiplication(0, 10), 0)

    def test_division(self):
        self.assertEqual(division(8, 4), 2)
        self.assertEqual(division(-8, 4), -2)
        self.assertEqual(division(0, 10), 0)
        self.assertIsNone(division(5, 0))  # La division par zéro devrait renvoyer None

if __name__ == '__main__':
    unittest.main()
