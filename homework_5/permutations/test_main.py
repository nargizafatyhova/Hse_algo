import io
import unittest
from contextlib import redirect_stdout

from main import permutations


class TestPermutations(unittest.TestCase):
    def test_three_elements(self):
        self.assertEqual(
            permutations([1, 2, 3]),
            [
                [1, 2, 3],
                [1, 3, 2],
                [2, 1, 3],
                [2, 3, 1],
                [3, 1, 2],
                [3, 2, 1],
            ],
        )

    def test_two_elements(self):
        self.assertEqual(permutations([0, 1]), [[0, 1], [1, 0]])

    def test_one_element(self):
        self.assertEqual(permutations([1]), [[1]])

    def test_empty_list(self):
        self.assertEqual(permutations([]), [[]])

    def test_input_is_not_changed(self):
        nums = [1, 2, 3]
        permutations(nums)
        self.assertEqual(nums, [1, 2, 3])

    def test_call_stack_visualization(self):
        output = io.StringIO()

        with redirect_stdout(output):
            result = permutations([1, 2], show_trace=True)

        lines = output.getvalue().splitlines()
        self.assertEqual(result, [[1, 2], [2, 1]])
        self.assertEqual(lines[0], "-> backtrack([1, 2], [])")
        self.assertTrue(any(line.startswith("    -> backtrack") for line in lines))
        self.assertEqual(lines[-1], "<- backtrack([1, 2], [])")


if __name__ == "__main__":
    unittest.main()
