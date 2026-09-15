import unittest

from main import is_palindrome


class TestPalindrome(unittest.TestCase):
    def test_true(self):
        for n in [1, 7, 11, 121, 1221, 1001]:
            self.assertTrue(is_palindrome(n))

    def test_false(self):
        for n in [10, 31, 1231]:
            self.assertFalse(is_palindrome(n))

    def test_not_positive(self):
        for n in [0, -1, -121]:
            self.assertFalse(is_palindrome(n))


if __name__ == "__main__":
    unittest.main()
