import unittest
import numpy as np
from array_operations import create_random_array, array_mean, array_std, elementwise_multiply, reshape_array

class TestArrayOperations(unittest.TestCase):
    def test_create_random_array(self):
        arr = create_random_array(10, 0, 100)
        self.assertEqual(len(arr), 10)
        self.assertTrue(all(0 <= x < 100 for x in arr))

    def test_array_mean(self):
        arr = np.array([1, 2, 3, 4, 5])
        self.assertEqual(array_mean(arr), 3.0)

    def test_array_std(self):
        arr = np.array([1, 2, 3, 4, 5])
        self.assertAlmostEqual(array_std(arr), 1.4142135623730951, places=7)

    def test_elementwise_multiply(self):
        arr1 = np.array([1, 2, 3])
        arr2 = np.array([4, 5, 6])
        result = elementwise_multiply(arr1, arr2)
        np.testing.assert_array_equal(result, np.array([4, 10, 18]))

    def test_reshape_array(self):
        arr = np.array([1, 2, 3, 4, 5, 6])
        reshaped = reshape_array(arr, (2, 3))
        np.testing.assert_array_equal(reshaped, np.array([[1, 2, 3], [4, 5, 6]]))

    def test_reshape_array_invalid_shape(self):
        arr = np.array([1, 2, 3, 4, 5])
        with self.assertRaises(ValueError):
            reshape_array(arr, (2, 3))

if __name__ == '__main__':
    unittest.main()