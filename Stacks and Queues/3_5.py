import unittest


class Stack(object):
    def __init__(self):
        self._storage = []

    def push(self, val):
        self._storage.append(val)

    def pop(self):
        return self._storage.pop()

    def __len__(self):
        return len(self._storage)


class MyQueue(object):
    def __init__(self):
        self._front = Stack()
        self._end = Stack()

    def _transfer(self):
        while self._end:
            self._front.push(self._end.pop())

    def enqueue(self, val):
        self._end.push(val)

    def deque(self):
        self._transfer()
        return self._front.pop()


class Test(unittest.TestCase):
    def setUp(self):
        self.que = MyQueue()

    def testEmpty(self):
        self.assertRaises(IndexError, self.que.deque)

    def testOneTimePush(self):
        for i in range(1000):
            self.que.enqueue(i)
        for i in range(1000):
            self.assertEqual(i, self.que.deque())

    def testMultiplePush(self):
        for i in range(1000):
            self.que.enqueue(i)
            self.assertEqual(i, self.que.deque())