import unittest
import List


def removeDuplicates(input_list):
    newList = List.LinkedList()
    val_set = set()
    for val in input_list:
        if val not in val_set:
            val_set.add(val)
            newList.append(val)
    return newList


def removeDupsInPlace(input_list):
    try:
        curNode = input_list.get(0)
        while curNode:
            remover = curNode
            while remover.next:
                # delete next element
                if remover.next.value == curNode.value:
                    # deletion
                    remover.next = remover.next.next
                else:
                    # only increment remover index when there is no node deleted
                    remover = remover.next
            curNode = curNode.next
    except IndexError:  # empty case
        pass


class Test(unittest.TestCase):
    def testRemoveDups(self):
        testList = List.LinkedList()
        for v in range(10):
            testList.append(v)
        # should not remove anything
        removed = removeDuplicates(testList)
        for i, e in enumerate(removed):
            self.assertEqual(i, e)
        # 10 elements
        self.assertEqual([i for i, e in enumerate(removed)], [i for i in range(10)])
        # add same elements again
        for v in range(10):
            testList.append(v)
        removed2 = removeDuplicates(testList)
        self.assertEqual([v for v in removed], [v for v in removed2])
        # create another list
        testList2 = List.LinkedList()
        for i in range(10):
            testList2.append(0)
        removed = removeDuplicates(testList2)
        # should only contain one element of 0
        self.assertEqual(removed.get(0).value, 0)
        self.assertRaises(IndexError, removed.get, 1)
        # empty case
        for val in removeDuplicates(List.LinkedList()):
            self.fail("Cannot enter here")

    def testInPlace(self):
        # empty case
        empty = List.LinkedList()
        removeDupsInPlace(empty)
        for val in empty:
            self.fail("Cannot enter here")

        testList = List.LinkedList()
        for v in range(10):
            testList.append(v)
        # should not remove anything
        removeDupsInPlace(testList)
        for i, e in enumerate(testList):
            self.assertEqual(i, e)
        # 10 elements
        self.assertEqual([i for i, e in enumerate(testList)], [i for i in range(10)])
        # add same elements again
        for v in range(10):
            testList.append(v)
        removeDupsInPlace(testList)
        self.assertEqual([i for i, e in enumerate(testList)], [i for i in range(10)])

        # create another list
        testList2 = List.LinkedList()
        for i in range(10):
            testList2.append(0)
        removeDupsInPlace(testList2)
        # should only contain one element of 0
        self.assertEqual(testList2.get(0).value, 0)
        self.assertRaises(IndexError, testList2.get, 1)

        # create another list
        testList2 = List.LinkedList()
        for i in range(10):
            testList2.append(i)
            testList2.append(i)
        removeDupsInPlace(testList2)
        self.assertEqual([i for i, e in enumerate(testList)], [i for i in range(10)])
