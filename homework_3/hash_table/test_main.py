import unittest

from main import HashTable


class KeyWithSameHash:
    def __init__(self, value):
        self.value = value

    def __hash__(self):
        return 1

    def __eq__(self, other):
        return isinstance(other, KeyWithSameHash) and self.value == other.value


class TestHashTable(unittest.TestCase):
    def test_put_and_get(self):
        table = HashTable()
        table.put("name", "Alice")
        table.put("age", 20)

        self.assertEqual(table.get("name"), "Alice")
        self.assertEqual(table.get("age"), 20)
        self.assertEqual(len(table), 2)

    def test_update(self):
        table = HashTable()
        table.put("a", 1)
        table.put("a", 2)

        self.assertEqual(table.get("a"), 2)
        self.assertEqual(len(table), 1)

    def test_collision(self):
        table = HashTable()
        first = KeyWithSameHash("first")
        second = KeyWithSameHash("second")

        table.put(first, 1)
        table.put(second, 2)

        self.assertEqual(table.get(first), 1)
        self.assertEqual(table.get(second), 2)

    def test_remove(self):
        table = HashTable()
        table.put("a", 1)

        self.assertEqual(table.remove("a"), 1)
        self.assertNotIn("a", table)
        self.assertEqual(len(table), 0)

    def test_missing_key(self):
        table = HashTable()

        with self.assertRaises(KeyError):
            table.get("missing")

        with self.assertRaises(KeyError):
            table.remove("missing")

    def test_resize_keeps_values(self):
        table = HashTable(capacity=2)

        for number in range(100):
            table.put(number, number * number)

        self.assertGreater(table.capacity, 2)

        for number in range(100):
            self.assertEqual(table.get(number), number * number)

    def test_shrink_keeps_values(self):
        table = HashTable(capacity=2)

        for number in range(20):
            table[number] = number

        grown_capacity = table.capacity

        for number in range(19):
            del table[number]

        self.assertLess(table.capacity, grown_capacity)
        self.assertEqual(table[19], 19)

    def test_square_brackets(self):
        table = HashTable()
        table["key"] = "value"

        self.assertEqual(table["key"], "value")
        self.assertIn("key", table)

    def test_invalid_capacity(self):
        with self.assertRaises(ValueError):
            HashTable(0)


if __name__ == "__main__":
    unittest.main()
