import unittest

from main import max_even_sum


class TestMaxEvenSum(unittest.TestCase):
    def test_cases(self):
        data = [
            ([5, 7, 13, 2, 14], 36),
            ([3], 0),
            ([2], 2),
            ([2, 4, 6], 12),
            ([1, 2, 4], 6),
            ([1, 3, 5], 8),
            ([7, 2, 9, 4], 22),
            ([], 0),
        ]

        for nums, expected in data:
            self.assertEqual(max_even_sum(nums), expected)


if __name__ == "__main__":
    unittest.main()
