import unittest


class SetOfStacks(object):
    def __init__(self, cap):
        # illegal value checking
        if cap <= 0:
            raise ValueError()
        self._capacity = cap
        # contains all the stacks
        self._stacks = []
        # create a new empty stack
        # as the current one
        self._curStack = []
        self._stacks.append(self._curStack)

    def push(self, val):
        if len(self._curStack) == self._capacity:
            self._curStack = [val]
            self._stacks.append(self._curStack)
        else:
            self._curStack.append(val)

    def pop(self):
        if len(self._curStack) == 0:
            # if the current one is the only one
            if len(self._stacks) == 1:
                raise IndexError()
            else:
                # get rid of the empty stack
                self._stacks.pop()
                # get the latest one
                self._curStack = self._stacks[-1]
        return self._curStack.pop()

    def popAt(self, idx):
        if 0 <= idx < len(self._stacks):
            # if this stack is empty, it will raise error
            # empty stack must be the last one
            res = self._stacks[idx].pop()
            # shift the following stacks if exist
            # putting all number in the buffer in a reversed order
            tmp = []
            for index in range(idx + 1, len(self._stacks)):
                cur = self._stacks[-1]
                while len(cur) != 0:
                    tmp.append(cur.pop())
                # delete the current empty stack
                self._stacks.pop()
            # assign the current stack to the last one
            # it must exist, which is 'idx'th
            self._curStack = self._stacks[-1]
            # use the built-in method to push
            # if will automatically calculate the capacity and current pointer
            while len(tmp) != 0:
                self.push(tmp.pop())
            # return the result
            return res
        else:
            raise IndexError()


class Test(unittest.TestCase):
    def testOneEmpty(self):
        s = SetOfStacks(1)
        self.assertRaises(IndexError, s.pop)
        self.assertRaises(IndexError, s.popAt, 0)
        self.assertRaises(IndexError, s.popAt, 1)
        self.assertRaises(IndexError, s.popAt, 2)

    def testOne(self):
        s = SetOfStacks(1)
        for i in range(5):
            s.push(i)
        for i in reversed(range(5)):
            self.assertEqual(i, s.pop())

        for i in range(5):
            s.push(i)
        for i in reversed(range(5)):
            self.assertEqual(i, s.popAt(i))

        for i in range(5):
            s.push(i)
        for i in range(5):
            self.assertEqual(i, s.popAt(0))

    def testTwo(self):
        s = SetOfStacks(2)
        data = [3, 3, 4, 4, 5, 5, 6, 6]
        for num in data:
            s.push(num)
        self.assertEqual(s.popAt(1), 4)
        self.assertEqual(s.popAt(1), 5)
        self.assertEqual(s.popAt(2), 6)
        self.assertEqual(s.popAt(2), 6)
        data2 = [5, 4, 3, 3]
        for i in range(4):
            self.assertEqual(s.pop(), data2[i])

        self.assertRaises(IndexError, s.pop)