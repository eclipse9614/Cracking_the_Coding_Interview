import unittest
from List import LinkedList


def delNode(input_list, pos):
    try:
        cur = input_list.get(pos)
    except IndexError:
        raise IndexError()
    # make sure that the current node is in the middle of the list
    if cur.next is None:
        raise IndexError()
    cur.value = cur.next.value
    cur.next = cur.next.next


class Test(unittest.TestCase):
    def testIllegalPos(self):
        testList = LinkedList()
        # populate
        testList.append(0)
        self.assertRaises(IndexError, delNode, testList, -1)
        self.assertRaises(IndexError, delNode, testList, 0)
        testList.append(1)
        delNode(testList, 0)
        self.assertEqual(testList.get(0).value, 1)
        self.assertRaises(IndexError, delNode, testList, 0)

    def testLegitPos(self):
        testList = LinkedList()
        for i in range(100):
            testList.append(i)
        mapping = range(100)
        for i in range(99):
            # keep deleting the first element
            delNode(testList, 0)
            del mapping[0]
            for i, e in enumerate(testList):
                self.assertEqual(e, mapping[i])