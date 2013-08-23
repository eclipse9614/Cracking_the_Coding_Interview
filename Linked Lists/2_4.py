import unittest
from List import LinkedList


def partition(input_list, partitioner):
    pre = LinkedList()
    post = LinkedList()
    for val in input_list:
        if val < partitioner:
            pre.append(val)
        else:
            post.append(val)
    # connecting pre and post lists
    pre.last.next = post.head.next
    return pre


def partitionInPlace(input_list, partitioner):
    # creates two fake nodes as insertion positions
    input_list.append(-1)
    pre = input_list.last
    input_list.append(-1)
    post = input_list.last
    # original list: head-1-3-4-5-7-8-...-pre-post
    # step: head-1-3-4-5-7-8-...-pre-1-2-3-post
    # step: head-1-3-4-5-7-8-...-pre-1-2-3-post-7-7-8
    # finally:head-pre-1-2-3-4-post-123-4-5-6-7-
    # delete both fake nodes
    # finally head-1-2-3-4-123-4-5-6-7
    head = input_list.head
    while head.next != pre:
        nextNode = head.next
        # remove next node from list
        head.next = nextNode.next
        # add next node to the back
        if nextNode.value < partitioner:
            nextNode.next = pre.next
            pre.next = nextNode
        else:
            nextNode.next = post.next
            post.next = nextNode

    # delete post
    if post.next:  # if there are trailing nodes after post
        # copy value
        # delete next node
        post.value = post.next.value
        post.next = post.next.next
    else:
        # loop from start
        while pre.next.next:
            pre = pre.next
        # now it is the pos before the post
        pre.next = None
    # delete pre
    input_list.head.next = pre.next


class Test(unittest.TestCase):
    def testEmptyList(self):
        empty = LinkedList()
        res = partition(empty, 0)
        self.assertRaises(IndexError, res.get, 0)
        partitionInPlace(empty, 1000)
        self.assertRaises(IndexError, empty.get, 0)

    def testNoPartition(self):
        testList = LinkedList()
        for i in range(10):
            testList.append(i)
        res = partition(testList, 0)
        res2 = partition(testList, 10)
        for i, v in enumerate(testList):
            self.assertEqual(v, res.get(i).value)
            self.assertEqual(v, res2.get(i).value)
        # second method
        partitionInPlace(testList, 0)
        mapping = range(10)
        for v in testList:
            # make sure every element in the partitioned
            # list has an equivalent in mapping
            self.assertTrue(v in mapping)
            mapping.remove(v)
        mapping = range(10)
        partitionInPlace(testList, 10)
        for v in testList:
            self.assertTrue(v in mapping)
            mapping.remove(v)

    def testPartition(self):
        testList = LinkedList()
        data = [1, 45, 28, 20, 60, 24, 24, 22, 2]
        for i in data:
            testList.append(i)
        res = partition(testList, 24)
        res_list = [v for v in res]
        self.assertEqual(res_list, [1, 20, 22, 2, 45, 28, 60, 24, 24])

        testList = LinkedList()
        data = [1, 1, 1, 1, 2]
        for i in data:
            testList.append(i)
        res = partition(testList, 1)
        res_list = [v for v in res]
        self.assertEqual(res_list, [1, 1, 1, 1, 2])

        # method 2
        testList = LinkedList()
        data = [-99, 100, 33, 44, -55, 78, 9, 8, 0]
        for d in data:
            testList.append(d)
        partitionInPlace(testList, 9)
        res = [v for v in testList]
        # [-99, -55, 0, 8]
        # [100, 33, 44, 78, 9]
        for i in range(4):
            self.assertTrue(res[i] < 9)
        for i in range(4, 9):
            self.assertTrue(res[i] >= 9)
        data.sort()
        res.sort()
        self.assertEqual(data, res)