# coding=utf-8
import unittest


def hasUniqueCharsGeneral(input_str):
    table = set()
    for ch in input_str:
        if ch in table:
            return False
        else:
            table.add(ch)
    return True


def hasUniqueCharsOnlyInAscII(input_str):
    table = [False] * 256
    for ch in input_str:
        val = ord(ch)
        if table[val]:
            return False
        else:
            table[val] = True
    return True


class Test(unittest.TestCase):
    def testGeneral(self):
        self.assertTrue(hasUniqueCharsGeneral("12345678"))
        self.assertTrue(hasUniqueCharsGeneral(u"abcdefg"))

        self.assertFalse(hasUniqueCharsGeneral(u"121"))
        self.assertFalse(hasUniqueCharsGeneral("123456778"))
        self.assertFalse(hasUniqueCharsGeneral("ajfkljie"))

        self.assertTrue(hasUniqueCharsGeneral(u"你好啊"))
        self.assertTrue(hasUniqueCharsGeneral(u"123你好啊abc"))
        self.assertFalse(hasUniqueCharsGeneral(u"啊啊"))

    def testAscII(self):
        self.assertTrue(hasUniqueCharsOnlyInAscII("1234567890"))
        self.assertTrue(hasUniqueCharsOnlyInAscII("abcdefghijklmnopqrstuvwxyz"))
        self.assertTrue(hasUniqueCharsOnlyInAscII("ABCDEFGHIJKLMNOPQRSTUVWXYZ"))

        self.assertFalse(hasUniqueCharsOnlyInAscII("11"))