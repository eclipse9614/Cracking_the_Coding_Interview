import unittest
import random
from circular_array import CircularArray


class Test(unittest.TestCase):
    def testIllegalSize(self):
        self.assertRaises(Exception, CircularArray, 0)
        self.assertRaises(Exception, CircularArray, -1)

    def testPushPop(self):
        cir = CircularArray(10)
        # try pop with empty array
        self.assertEqual(cir.pop(), None)
        # since this is a circular array
        # it should support multiple fill out and clear
        for j in range(10):
            # push ten elements
            for i in range(10):
                self.assertEqual(cir.push(i), True)
            # it is full, it should return false
            # means fail to push again
            self.assertEqual(cir.push(1), False)
            for i in range(10):
                self.assertEqual(i, cir.pop())
        # it should support push and pop right after each other
        for i in range(100):
            ran = random.randint(-10000, 10000)
            self.assertEqual(cir.push(ran), True)
            self.assertEqual(cir.pop(), ran)

    def testState(self):
        cir = CircularArray(5)
        self.assertEqual(cir.isEmpty(), True)
        self.assertEqual(cir.isFull(), False)
        cir.push('A')
        self.assertEqual(cir.isEmpty(), False)
        self.assertEqual(cir.isFull(), False)
        cir.push('B')
        self.assertEqual(cir.isEmpty(), False)
        self.assertEqual(cir.isFull(), False)
        cir.push('C')
        self.assertEqual(cir.isEmpty(), False)
        self.assertEqual(cir.isFull(), False)
        cir.push('D')
        self.assertEqual(cir.isEmpty(), False)
        self.assertEqual(cir.isFull(), False)
        cir.push('E')
        self.assertEqual(cir.isEmpty(), False)
        self.assertEqual(cir.isFull(), True)
        # pop
        self.assertEqual(cir.pop(), 'A')
        self.assertEqual(cir.isEmpty(), False)
        self.assertEqual(cir.isFull(), False)
        self.assertEqual(cir.pop(), 'B')
        self.assertEqual(cir.isEmpty(), False)
        self.assertEqual(cir.isFull(), False)
        self.assertEqual(cir.pop(), 'C')
        self.assertEqual(cir.isEmpty(), False)
        self.assertEqual(cir.isFull(), False)
        self.assertEqual(cir.pop(), 'D')
        self.assertEqual(cir.isEmpty(), False)
        self.assertEqual(cir.isFull(), False)
        self.assertEqual(cir.pop(), 'E')
        self.assertEqual(cir.isEmpty(), True)
        self.assertEqual(cir.isFull(), False)
        self.assertEqual(cir.pop(), None)
        self.assertEqual(cir.isEmpty(), True)
        self.assertEqual(cir.isFull(), False)