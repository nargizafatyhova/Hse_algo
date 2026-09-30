import unittest

from main import validate_stack_sequences


class TestValidateStackSequences(unittest.TestCase):
    def test_true_example(self):
        pushed = [1, 2, 3, 4, 5]
        popped = [1, 3, 5, 4, 2]

        self.assertTrue(validate_stack_sequences(pushed, popped))

    def test_false_example(self):
        pushed = [1, 2, 3]
        popped = [3, 1, 2]

        self.assertFalse(validate_stack_sequences(pushed, popped))

    def test_reverse_order(self):
        self.assertTrue(validate_stack_sequences([1, 2, 3], [3, 2, 1]))

    def test_same_order(self):
        self.assertTrue(validate_stack_sequences([1, 2, 3], [1, 2, 3]))

    def test_one_element(self):
        self.assertTrue(validate_stack_sequences([10], [10]))

    def test_different_lengths(self):
        self.assertFalse(validate_stack_sequences([1, 2], [1]))

    def test_large_input(self):
        pushed = list(range(100_000))
        popped = list(reversed(pushed))

        self.assertTrue(validate_stack_sequences(pushed, popped))


if __name__ == "__main__":
    unittest.main()
