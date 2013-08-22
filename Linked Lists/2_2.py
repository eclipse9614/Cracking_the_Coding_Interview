import unittest
from List import LinkedList


def lastKthElement(input_list, k):
    try:
        leader = input_list.get(k)
    except IndexError:
        return None
    follower = input_list.get(0)
    while leader.next:
        leader = leader.next
        follower = follower.next
    return follower


class Test(unittest.TestCase):
    def test(self):
        testList = LinkedList()
        # populate
        for i in range(5):
            testList.append(i)
        # 5th to 10th should be None, because 0-1-2-3-4, 5th is beyond the first element
        for i in range(10, 4, -1):
            self.assertEqual(lastKthElement(testList, i), None)
        # 0th to 4th should not be None
        for i in range(4, -1, -1):
            self.assertEqual(lastKthElement(testList, i).value, 4 - i)
        # negative index
        for i in range(-10, 0):
            self.assertEqual(lastKthElement(testList, i), None)