import io
import unittest
from contextlib import redirect_stdout

from main import trace


class TestTracer(unittest.TestCase):
    def test_recursive_calls(self):
        @trace
        def factorial(n):
            if n <= 1:
                return 1
            return n * factorial(n - 1)

        output = io.StringIO()
        with redirect_stdout(output):
            result = factorial(3)

        self.assertEqual(result, 6)
        self.assertEqual(
            output.getvalue().splitlines(),
            [
                "-> factorial(3)",
                "  -> factorial(2)",
                "    -> factorial(1)",
                "    <- factorial(1) = 1",
                "  <- factorial(2) = 2",
                "<- factorial(3) = 6",
            ],
        )

    def test_keyword_arguments(self):
        @trace
        def add(a, b=0):
            return a + b

        output = io.StringIO()
        with redirect_stdout(output):
            result = add(2, b=3)

        self.assertEqual(result, 5)
        self.assertIn("add(2, b=3)", output.getvalue())

    def test_function_metadata_is_saved(self):
        @trace
        def example():
            """Example documentation."""
            return None

        self.assertEqual(example.__name__, "example")
        self.assertEqual(example.__doc__, "Example documentation.")

    def test_depth_is_reset_after_exception(self):
        @trace
        def fail(should_fail):
            if should_fail:
                raise ValueError("error")
            return "ok"

        output = io.StringIO()
        with redirect_stdout(output):
            with self.assertRaises(ValueError):
                fail(True)
            self.assertEqual(fail(False), "ok")

        self.assertIn("\n-> fail(False)\n", "\n" + output.getvalue())


if __name__ == "__main__":
    unittest.main()
