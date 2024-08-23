import unittest
from list_operations import find_max, remove_duplicates, sum_even_numbers

class TestListOperations(unittest.TestCase):
    def test_find_max(self):
        self.assertEqual(find_max([1, 5, 3, 9, 2]), 9)
        self.assertEqual(find_max([-1, -5, -3]), -1)
        self.assertEqual(find_max([0]), 0)

    def test_find_max_empty_list(self):
        with self.assertRaises(ValueError):
            find_max([])

    def test_remove_duplicates(self):
        self.assertEqual(remove_duplicates([1, 2, 2, 3, 4, 4, 5]), [1, 2, 3, 4, 5])
        self.assertEqual(remove_duplicates([1, 1, 1, 1]), [1])
        self.assertEqual(remove_duplicates([]), [])

    def test_sum_even_numbers(self):
        self.assertEqual(sum_even_numbers([1, 2, 3, 4, 5, 6]), 12)
        self.assertEqual(sum_even_numbers([1, 3, 5, 7]), 0)
        self.assertEqual(sum_even_numbers([]), 0)

if __name__ == '__main__':
    unittest.main()