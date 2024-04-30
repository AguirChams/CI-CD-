import unittest
from calculator import p_expression_binop  # Replace 'your_module' with the actual module name where your function is defined

class TestExpression(unittest.TestCase):
    def test_addition(self):
        t = [1, '+', 2]
        p_expression_binop(t)
        self.assertEqual(t[0], 3)

    def test_subtraction(self):
        t = [5, '-', 3]
        p_expression_binop(t)
        self.assertEqual(t[0], 2)

    def test_multiplication(self):
        t = [4, '*', 6]
        p_expression_binop(t)
        self.assertEqual(t[0], 24)

    def test_division(self):
        t = [10, '/', 2]
        p_expression_binop(t)
        self.assertEqual(t[0], 5)

if __name__ == '__main__':
    unittest.main()
