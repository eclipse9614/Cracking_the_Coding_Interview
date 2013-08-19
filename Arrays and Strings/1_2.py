import unittest


def reverseStr(input_str):
    reversedList = list(input_str)
    reversedList.reverse()
    return "".join(reversedList)


class Test(unittest.TestCase):
    def testReverse(self):
        self.assertEqual("", reverseStr(""))
        self.assertEqual("1", reverseStr("1"))
        self.assertEqual("2", reverseStr("2"))
        self.assertEqual("av", reverseStr("va"))
        self.assertEqual("ava", reverseStr("ava"))
        self.assertEqual("abcd", reverseStr("dcba"))
        self.assertEqual("123456789", reverseStr("987654321"))