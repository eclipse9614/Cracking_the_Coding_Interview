import unittest
from List import LinkedList, Node


def addTwoLists(first, second):
    firstRunner = first.head
    secondRunner = second.head
    result = LinkedList()
    residue = 0
    while firstRunner.next or secondRunner.next or residue == 1:
        # process the first runner
        # it will keep going only if it has a next pointer
        if firstRunner.next:
            firstValue = firstRunner.next.value
            firstRunner = firstRunner.next
        else:
            firstValue = 0
        # process the second one
        if secondRunner.next:
            secondValue = secondRunner.next.value
            secondRunner = secondRunner.next
        else:
            secondValue = 0
        # calculate the sum
        sumV = firstValue + secondValue + residue
        # check whether it is too big for single digit
        if sumV > 9:
            sumV -= 10
            residue = 1
        else:
            residue = 0
        result.append(sumV)
    return result


def reverseList(input_list):
    newList = LinkedList()
    content = reversed([v for v in input_list])
    for v in content:
        newList.append(v)
    return newList


def addTwoListsReversed(first, second):
    reversed1 = reverseList(first)
    reversed2 = reverseList(second)
    res = addTwoLists(reversed1, reversed2)
    return reverseList(res)


class Test(unittest.TestCase):
    def testAddEmpty(self):
        # two empty lists
        empty1 = LinkedList()
        empty2 = LinkedList()
        empty3 = addTwoLists(empty1, empty2)
        self.assertEqual(empty3.head.next, None)
        # only one empty list
        nonEmpty = LinkedList()
        nonEmpty.append(1)
        res = addTwoLists(empty1, nonEmpty)
        self.assertEqual(res.head.next.value, 1)
        self.assertEqual(res.head.next.next, None)
        res = addTwoLists(nonEmpty, empty1)
        self.assertEqual(res.head.next.value, 1)
        self.assertEqual(res.head.next.next, None)

    def testAddSimple(self):
        listA = LinkedList()
        listB = LinkedList()
        listA.append(1)
        listA.append(2)
        listA.append(3)
        listB.append(4)
        listB.append(5)
        listB.append(6)
        res = addTwoLists(listA, listB)
        content = [v for v in res]
        self.assertEqual(content, [5, 7, 9])

    def testAddHard(self):
        contentA = [5, 6, 7, 1]
        contentB = [5, 3, 2]
        listA = LinkedList()
        listB = LinkedList()
        for v in contentA:
            listA.append(v)
        for v in contentB:
            listB.append(v)
        contentC = [0, 0, 0, 2]
        listC = addTwoLists(listA, listB)
        self.assertEqual([v for v in listC], contentC)

        # second case
        contentA = [5]
        contentB = [6]
        listA = LinkedList()
        listB = LinkedList()
        for v in contentA:
            listA.append(v)
        for v in contentB:
            listB.append(v)
        contentC = [1, 1]
        listC = addTwoLists(listA, listB)
        self.assertEqual([v for v in listC], contentC)

    def testReversing(self):
        # empty
        empty = LinkedList()
        res = reverseList(empty)
        self.assertEqual(res.head.next, None)
        # one element
        empty.append(99)
        res = reverseList(empty)
        self.assertEqual(res.head.next.value, 99)
        self.assertEqual(res.head.next.next, None)
        # multiple elements
        empty.append(1)
        res = reverseList(empty)
        content = [1, 99]
        self.assertEqual([v for v in res], content)