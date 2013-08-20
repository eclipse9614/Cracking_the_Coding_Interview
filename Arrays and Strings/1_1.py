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


def hasUniqueCharsOnlyInAscII2(input_str):
    storage = [0] * 8
    for ch in input_str:
        val = ord(ch)
        index = val / 32
        remainder = val - index * 32
        if storage[index] & 2 ** remainder:
            return False
        else:
            storage[index] += 2 ** remainder
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
        self.assertTrue(hasUniqueCharsOnlyInAscII("".join([chr(i) for i in range(0, 256)])))
        self.assertFalse(hasUniqueCharsOnlyInAscII("11"))

    def testAscII2(self):
        self.assertTrue(hasUniqueCharsOnlyInAscII2("1234567890"))
        self.assertTrue(hasUniqueCharsOnlyInAscII2("abcdefghijklmnopqrstuvwxyz"))
        self.assertTrue(hasUniqueCharsOnlyInAscII2("ABCDEFGHIJKLMNOPQRSTUVWXYZ"))
        self.assertTrue(hasUniqueCharsOnlyInAscII2("".join([chr(i) for i in range(0, 256)])))
        self.assertFalse(hasUniqueCharsOnlyInAscII2("11"))