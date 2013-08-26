import unittest
from List import LinkedList


def findLoopEntry(looped_list):
    """
    Take advantage of set class
    :param looped_list: corrupted list
    :return: the intertwined node if exists
    """
    table = set()
    runner = looped_list.head
    while runner.next:
        addr = id(runner.next)
        if addr in table:
            return runner.next
        else:
            table.add(addr)
            runner = runner.next
    return None


def findLoopEntrySmart(looped_list):
    """
    having two runners at start, they will meet eventually
    the distances difference is n * len(lap)
    d1: start to intertwined
    d2: intertwined to meeting node
    2 * (d1 + d2) = d1 + d2 + n * len(lap)
    d1 + d2 = n * len(lap)
    d1 = (n - 1) * len(lap) + (len(lap) - d2) (n >= 1 since step2runner is faster)
    to find the length of d1, simply do a fresh new runner and a continued runner each from start and meeting node
    they will meet at intertwined node
    :param looped_list:
    :return: the intertwined node if exists
    """
    step1runner = looped_list.head
    step2runner = looped_list.head
    # find meeting node
    while True:
        try:
            step1runner = step1runner.next
            step2runner = step2runner.next.next
            if step1runner is step2runner:
                meetingNode = step1runner
                break
        except AttributeError:
            return None  # this is not a corrupted list
    # find intertwined node
    freshRunner = looped_list.head
    continuedRunner = meetingNode
    while freshRunner is not continuedRunner:
        freshRunner = freshRunner.next
        continuedRunner = continuedRunner.next
    return freshRunner


class Test(unittest.TestCase):
    def setUp(self):
        self.methods = [findLoopEntry, findLoopEntrySmart]

    def testNormalLists(self):
        # both methods should return None
        a = LinkedList()
        for method in self.methods:
            self.assertEqual(method(a), None)
        # non empty
        a.append(9)
        a.append(6)
        a.append(3)
        for method in self.methods:
            self.assertEqual(method(a), None)

    def testCorruptedLists(self):
        # A->B->C->D->E->C
        a = LinkedList()
        a.append('A')
        a.append('B')
        a.append('C')
        intertwined = a.last
        a.append('D')
        a.append('E')
        a.last.next = intertwined
        for method in self.methods:
            self.assertEqual(method(a), intertwined)
        # A->A
        b = LinkedList()
        b.append('A')
        intertwined = b.last
        b.last.next = intertwined
        for method in self.methods:
            self.assertEqual(method(b), intertwined)