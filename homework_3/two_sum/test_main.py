import unittest

from main import two_sum


class TestTwoSum(unittest.TestCase):
    def test_example(self):
        self.assertEqual(two_sum([1, 3, 4, 10], 7), (1, 2))

    def test_equal_values(self):
        self.assertEqual(two_sum([5, 5, 1, 4], 10), (0, 1))

    def test_negative_values(self):
        self.assertEqual(two_sum([-8, 2, 7, 11], -1), (0, 2))

    def test_zero(self):
        self.assertEqual(two_sum([0, 4, 3, 1], 4), (0, 1))

    def test_pair_at_the_ends(self):
        self.assertEqual(two_sum([10, 2, 3, -4], 6), (0, 3))

    def test_pair_not_found(self):
        with self.assertRaises(ValueError):
            two_sum([1, 2, 3], 10)


if __name__ == "__main__":
    unittest.main()
