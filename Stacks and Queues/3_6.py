import random
import unittest


class Stack(object):
    def __init__(self):
        self._storage = []

    def push(self, val):
        self._storage.append(val)

    def pop(self):
        return self._storage.pop()

    def peep(self):
        return self._storage[-1]

    def isEmpty(self):
        return len(self._storage) == 0

    def topDown(self):
        return [val for val in reversed(self._storage)]


def sort(stack):
    buff = Stack()
    while not stack.isEmpty():
        # get the top element
        top = stack.pop()
        # put the ones smaller than top back to original stack
        while not buff.isEmpty() and top > buff.peep():
            stack.push(buff.pop())
        # put the top back to buffer
        buff.push(top)
    # push all elements back
    while not buff.isEmpty():
        stack.push(buff.pop())


class Test(unittest.TestCase):
    def test(self):
        data = [random.randint(-1000, i) for i in range(1000)]
        a = Stack()
        for val in data:
            a.push(val)

        data.sort(reverse=True)
        sort(a)
        self.assertEqual(a.topDown(), data)