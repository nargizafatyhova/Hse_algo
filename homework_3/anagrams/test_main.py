import unittest

from main import group_anagrams


def normalize(groups):
    return sorted(sorted(group) for group in groups)


class TestGroupAnagrams(unittest.TestCase):
    def test_example(self):
        words = ["eat", "tea", "tan", "ate", "nat", "bat"]
        expected = [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]]

        self.assertEqual(normalize(group_anagrams(words)), normalize(expected))

    def test_empty_list(self):
        self.assertEqual(group_anagrams([]), [])

    def test_empty_string(self):
        self.assertEqual(group_anagrams([""]), [[""]])

    def test_repeated_words(self):
        words = ["abc", "abc", "bca"]

        self.assertEqual(group_anagrams(words), [["abc", "abc", "bca"]])

    def test_different_lengths_and_register(self):
        words = ["a", "ab", "ba", "A"]
        expected = [["a"], ["ab", "ba"], ["A"]]

        self.assertEqual(normalize(group_anagrams(words)), normalize(expected))


if __name__ == "__main__":
    unittest.main()
