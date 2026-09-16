import unittest

from main import count_primes


class TestCountPrimes(unittest.TestCase):
    def test_cases(self):
        data = [
            (0, 0),
            (1, 0),
            (2, 0),
            (3, 1),
            (4, 2),
            (10, 4),
            (20, 8),
            (100, 25),
        ]

        for n, expected in data:
            self.assertEqual(count_primes(n), expected)


if __name__ == "__main__":
    unittest.main()
