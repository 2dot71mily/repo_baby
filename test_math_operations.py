import unittest
from math_operations import add, subtract, multiply, divide, chain_operations


class TestMathOperations(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(0, 0), 0)

    def test_subtract(self):
        self.assertEqual(subtract(5, 3), 2)
        self.assertEqual(subtract(10, 15), -5)
        self.assertEqual(subtract(0, 0), 0)

    def test_multiply(self):
        self.assertEqual(multiply(2, 3), 6)
        self.assertEqual(multiply(-2, 4), -8)
        self.assertEqual(multiply(0, 5), 0)

    def test_divide(self):
        self.assertEqual(divide(6, 3), 2)
        self.assertEqual(divide(10, 2), 5)
        self.assertAlmostEqual(divide(1, 3), 0.3333333, places=6)

    def test_divide_by_zero(self):
        with self.assertRaises(ValueError):
            divide(5, 0)


class TestChainOperations(unittest.TestCase):
    def test_chain_operations(self):
        x, y = 10, 5
        operations = [add, multiply, subtract, divide]
        expected_result = ((10 + 5) * 5 - 5) / 5
        self.assertAlmostEqual(chain_operations(x, y, operations), expected_result)

    def test_chain_operations_zero_division(self):
        x, y = 10, 0
        operations = [add, multiply, divide]
        with self.assertRaises(ValueError):
            chain_operations(x, y, operations)


if __name__ == "__main__":
    unittest.main()
