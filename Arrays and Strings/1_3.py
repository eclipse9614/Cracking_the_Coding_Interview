# coding=utf-8
import unittest


def isPermutation(str_a, str_b):
    if len(str_a) != len(str_b):
        return False
    listed_a = list(str_a)
    listed_b = list(str_b)
    listed_a.sort()
    listed_b.sort()
    return listed_a == listed_b


def isPermutationAscII(str_a, str_b):
    if len(str_a) != len(str_b):
        return False
    table_a = [0] * 256
    table_b = [0] * 256
    for ch in str_a:
        table_a[ord(ch)] += 1
    for ch in str_b:
        table_b[ord(ch)] += 1
    return table_a == table_b


class Test(unittest.TestCase):
    def testIsPermutation(self):
        self.assertTrue(isPermutation("abc", "abc"))
        self.assertTrue(isPermutation("1", "1"))
        self.assertTrue(isPermutation("", ""))
        self.assertTrue(isPermutation(u"你好啊", u"啊你好"))
        self.assertTrue(isPermutation("poi", "iop"))
        self.assertTrue(isPermutation("good morning", "morninggoo d"))
        self.assertTrue(isPermutation("123456", "654231"))
        # false
        self.assertFalse(isPermutation("ba", "bac"))
        self.assertFalse(isPermutation("abc", "de"))
        self.assertFalse(isPermutation("12345", "67890"))

    def testIsPermutationAscII(self):
        self.assertTrue(isPermutationAscII("abc", "abc"))
        self.assertTrue(isPermutationAscII("1", "1"))
        self.assertTrue(isPermutationAscII("", ""))
        self.assertTrue(isPermutationAscII("poi", "iop"))
        self.assertTrue(isPermutationAscII("good morning", "morninggoo d"))
        self.assertTrue(isPermutation("123456", "654231"))
        # false
        self.assertFalse(isPermutationAscII("ba", "bac"))
        self.assertFalse(isPermutationAscII("abc", "de"))
        self.assertFalse(isPermutationAscII("12345", "67890"))