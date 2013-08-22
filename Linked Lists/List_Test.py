import unittest
import List


class TestList(unittest.TestCase):
    def setUp(self):
        self.list = List.LinkedList()

    def testInit(self):
        self.assertIs(self.list.head.next, None)
        self.assertIs(self.list.head.value, None)
        self.assertIs(self.list.head, self.list.last)

    def testAppending(self):
        curList = self.list
        curList.append(1)
        curList.append(2)
        curList.append(3)
        self.assertEqual(curList.last.value, 3)
        self.assertEqual(curList.head.value, None)
        self.assertEqual(curList.head.next.value, 1)
        self.assertEqual(curList.head.next.next.value, 2)

    def testInsert(self):
        curList = self.list
        # illegal operation
        self.assertRaises(IndexError, curList.insert, 1, 10)
        self.assertRaises(IndexError, curList.insert, 2, 10)
        self.assertRaises(IndexError, curList.insert, 3, 10)
        # legal operation
        curList.insert(0, 10)
        curList.insert(0, 100)
        curList.insert(0, 1000)
        self.assertEqual(curList.head.value, None)
        self.assertEqual(curList.head.next.value, 1000)
        self.assertEqual(curList.head.next.next.value, 100)
        self.assertEqual(curList.last.value, 10)
        curList.insert(1, 999)
        self.assertEqual(curList.head.value, None)
        self.assertEqual(curList.head.next.value, 1000)
        self.assertEqual(curList.head.next.next.value, 999)
        self.assertEqual(curList.head.next.next.next.value, 100)
        self.assertEqual(curList.last.value, 10)
        # insert into last position
        curList.insert(4, 1)
        self.assertEqual(curList.last.value, 1)
        self.assertEqual(curList.head.next.next.next.next.value, 10)

    def testGet(self):
        curList = self.list
        # append 100 nodes
        for x in range(100):
            curList.append(x ** 2)
        for x in range(100):
            self.assertEqual(curList.get(x).value, x ** 2)
        for x in range(100, 105):
            self.assertRaises(IndexError, curList.get, x)

    def testDelete(self):
        curList = self.list
        # illegal
        for i in range(10):
            self.assertRaises(IndexError, curList.delete, i)
        # append 100 nodes after head
        for x in range(100):
            curList.append(x)
        res = [i for i in range(100)]
        # delete 99, 50, 49, 38, 20, 18, 11, 5, 0
        deleted = [99, 50, 49, 38, 20, 18, 11, 5, 0]
        for i in deleted:
            curList.delete(i)
            del res[i]
        for pos, element in enumerate(res):
            self.assertEqual(curList.get(pos), element)

    def testIteration(self):
        curList = self.list
        for x in curList:
            self.fail("Should not enter here since it is empty")
        for x in range(100):
            curList.append(x)
        for i, element in enumerate(curList):
            self.assertEqual(i, element)