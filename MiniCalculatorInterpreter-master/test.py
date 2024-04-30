import unittest
from calculator import addition  # Replace 'your_module' with the actual module name where your function is defined
class TestAddition(unittest.TestCase):
    def test_addition_positive_numbers(self):
        result = addition(3, 5)
        self.assertEqual(result, 8)

    def test_addition_negative_numbers(self):
        result = addition(-3, -5)
        self.assertEqual(result, -8)

    def test_addition_mixed_numbers(self):
        result = addition(3, -5)
        self.assertEqual(result, -2)

    def test_addition_zero(self):
        result = addition(0, 5)
        self.assertEqual(result, 5)


if __name__ == '__main__':
    unittest.main()
