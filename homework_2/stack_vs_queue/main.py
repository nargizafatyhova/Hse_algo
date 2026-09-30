class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Stack:
    def __init__(self):
        self.head = None
        self.size = 0

    def push(self, value):
        node = Node(value)
        node.next = self.head
        self.head = node
        self.size += 1

    def pop(self):
        if self.is_empty():
            raise IndexError("pop from empty stack")

        value = self.head.value
        self.head = self.head.next
        self.size -= 1
        return value

    def peek(self):
        if self.is_empty():
            raise IndexError("peek from empty stack")

        return self.head.value

    def is_empty(self):
        return self.head is None

    def __len__(self):
        return self.size


class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def enqueue(self, value):
        node = Node(value)

        if self.is_empty():
            self.head = node
        else:
            self.tail.next = node

        self.tail = node
        self.size += 1

    def dequeue(self):
        if self.is_empty():
            raise IndexError("dequeue from empty queue")

        value = self.head.value
        self.head = self.head.next
        self.size -= 1

        if self.head is None:
            self.tail = None

        return value

    def peek(self):
        if self.is_empty():
            raise IndexError("peek from empty queue")

        return self.head.value

    def is_empty(self):
        return self.head is None

    def __len__(self):
        return self.size
