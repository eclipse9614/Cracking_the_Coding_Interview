import unittest


class Tower(object):
    """
        A wrapper for hanoi tower based on built-in list
    """
    def __init__(self):
        self._storage = []

    def push(self, val):
        self._storage.append(val)

    def pop(self):
        return self._storage.pop()

    def topDown(self):
        return [val for val in reversed(self._storage)]


class Hanoi(object):
    def __init__(self, val):
        if val <= 0:
            raise ValueError()
        self._a = Tower()
        self._b = Tower()
        self._c = Tower()
        self._populateTowerA(val)

    def _move(self, start, end):
        end.push(start.pop())

    def _moveTo(self, start, end, buff, levels):
        if levels != 0:
            self._moveTo(start, buff, end, levels - 1)
            self._move(start, end)
            self._moveTo(buff, end, start, levels - 1)

    def _populateTowerA(self, val):
        for i in reversed(range(val)):
            self._a.push(i)

    def moveFromAtoC(self):
        self._moveTo(self._a, self._c, self._b, len(self._a.topDown()))
        return self._c.topDown()


class Test(unittest.TestCase):
    def test(self):
        self.assertRaises(ValueError, Hanoi, 0)
        for i in range(1, 20):
            hanoi = Hanoi(i)
            self.assertEqual(hanoi.moveFromAtoC(), range(i))