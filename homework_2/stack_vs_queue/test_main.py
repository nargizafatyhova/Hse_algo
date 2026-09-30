import unittest

from main import Queue, Stack


class TestStack(unittest.TestCase):
    def test_lifo_order(self):
        stack = Stack()

        for value in [1, 2, 3]:
            stack.push(value)

        self.assertEqual(stack.pop(), 3)
        self.assertEqual(stack.pop(), 2)
        self.assertEqual(stack.pop(), 1)

    def test_peek_does_not_remove_element(self):
        stack = Stack()
        stack.push(10)

        self.assertEqual(stack.peek(), 10)
        self.assertEqual(len(stack), 1)

    def test_empty_stack(self):
        stack = Stack()

        self.assertTrue(stack.is_empty())
        self.assertEqual(len(stack), 0)

        with self.assertRaises(IndexError):
            stack.pop()

        with self.assertRaises(IndexError):
            stack.peek()


class TestQueue(unittest.TestCase):
    def test_fifo_order(self):
        queue = Queue()

        for value in [1, 2, 3]:
            queue.enqueue(value)

        self.assertEqual(queue.dequeue(), 1)
        self.assertEqual(queue.dequeue(), 2)
        self.assertEqual(queue.dequeue(), 3)

    def test_queue_can_be_filled_again(self):
        queue = Queue()
        queue.enqueue(1)
        self.assertEqual(queue.dequeue(), 1)

        queue.enqueue(2)

        self.assertEqual(queue.peek(), 2)
        self.assertEqual(len(queue), 1)
        self.assertFalse(queue.is_empty())

    def test_empty_queue(self):
        queue = Queue()

        self.assertTrue(queue.is_empty())
        self.assertEqual(len(queue), 0)

        with self.assertRaises(IndexError):
            queue.dequeue()

        with self.assertRaises(IndexError):
            queue.peek()


if __name__ == "__main__":
    unittest.main()
