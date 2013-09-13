import unittest


class Stack(object):
    def __init__(self):
        self._storage = []
        self._mins = []

    def push(self, val):
        self._storage.append(val)
        if len(self._mins) == 0 or val < self._mins[-1]:
            self._mins.append(val)
        else:
            self._mins.append(self._mins[-1])

    def pop(self):
        self._mins.pop()
        return self._storage.pop()

    def min(self):
        return self._mins[-1]


class Test(unittest.TestCase):
    def testEmpty(self):
        s = Stack()
        self.assertRaises(IndexError, s.pop)
        self.assertRaises(IndexError, s.min)

    def test(self):
        s = Stack()
        for i in range(5):
            s.push(i)
            self.assertEqual(s.min(), 0)
        for i in reversed(range(4)):
            self.assertEqual(s.pop(), i + 1)
            self.assertEqual(s.min(), 0)
        self.assertEqual(s.pop(), 0)
        self.assertRaises(IndexError, s.min)

    def test2(self):
        s = Stack()
        for i in reversed(range(5)):
            s.push(i)
            self.assertEqual(s.min(), i)
        for i in range(5):
            self.assertEqual(s.min(), i)
            self.assertEqual(s.pop(), i)

    def test3(self):
        s = Stack()
        data = [9, 2, 5, 3, 0]
        mins = [9, 2, 2, 2, 0]
        for i, v in enumerate(data):
            s.push(v)
            self.assertEqual(s.min(), mins[i])