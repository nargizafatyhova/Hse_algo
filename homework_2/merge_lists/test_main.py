import unittest

from main import ListNode, merge_lists_with_dummy, merge_lists_without_dummy


def make_linked_list(values):
    head = None

    for value in reversed(values):
        head = ListNode(value, head)

    return head


def linked_list_to_list(head):
    values = []

    while head is not None:
        values.append(head.value)
        head = head.next

    return values


class MergeListsTests:
    merge = None

    def test_example(self):
        list1 = make_linked_list([1, 2, 4])
        list2 = make_linked_list([1, 3, 4])

        result = self.merge(list1, list2)

        self.assertEqual(linked_list_to_list(result), [1, 1, 2, 3, 4, 4])

    def test_empty_lists(self):
        self.assertIsNone(self.merge(None, None))

    def test_one_empty_list(self):
        list1 = make_linked_list([1, 2, 3])

        result = self.merge(list1, None)

        self.assertIs(result, list1)
        self.assertEqual(linked_list_to_list(result), [1, 2, 3])

    def test_different_lengths_and_negative_values(self):
        list1 = make_linked_list([-5, 2, 10, 15])
        list2 = make_linked_list([-3, 0])

        result = self.merge(list1, list2)

        self.assertEqual(linked_list_to_list(result), [-5, -3, 0, 2, 10, 15])

    def test_original_nodes_are_used(self):
        list1 = make_linked_list([1, 3])
        list2 = make_linked_list([2, 4])
        original_nodes = {list1, list1.next, list2, list2.next}

        result = self.merge(list1, list2)
        result_nodes = set()

        while result is not None:
            result_nodes.add(result)
            result = result.next

        self.assertEqual(result_nodes, original_nodes)


class TestMergeWithDummy(MergeListsTests, unittest.TestCase):
    merge = staticmethod(merge_lists_with_dummy)


class TestMergeWithoutDummy(MergeListsTests, unittest.TestCase):
    merge = staticmethod(merge_lists_without_dummy)


if __name__ == "__main__":
    unittest.main()
