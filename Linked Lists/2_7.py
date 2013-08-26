import unittest
from List import LinkedList


def isPalindrome(input_list):
    normal = [v for v in input_list]
    reverse = list(normal)
    reverse.reverse()
    return normal == reverse


class Test(unittest.TestCase):
    def test(self):
        # empty
        a = LinkedList()
        self.assertTrue(isPalindrome(a))
        # one element
        a.append("C")
        self.assertTrue(isPalindrome(a))
        # two elements
        a.append("A")
        self.assertFalse(isPalindrome(a))
        # three elements
        a.append("C")
        self.assertTrue(isPalindrome(a))