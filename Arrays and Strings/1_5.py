import unittest


class Bucket(object):
    def __init__(self, char):
        self._char = char
        self._count = 1

    def __str__(self):
        return self._char + str(self._count)

    def addOne(self):
        self._count += 1


def compression(input_str):
    """
    perform basic string compression using the counts of repeated characters
    :param input_str: original string
    :return: compressed string or original string if compressed one is larger
    """
    table = []
    lastCh = None
    lastIndex = -1
    for ch in input_str:
        if ch == lastCh:
            table[lastIndex].addOne()
        else:
            lastCh = ch
            lastIndex += 1
            table.append(Bucket(lastCh))
    candidate = "".join([str(bucket) for bucket in table])
    return candidate if len(candidate) < len(input_str) else input_str


class Test(unittest.TestCase):
    def testCompression(self):
        self.assertEqual(compression(""), "")
        self.assertEqual(compression("a"), "a")
        self.assertEqual(compression("aa"), "aa")
        self.assertEqual(compression("aaa"), "a3")
        self.assertEqual(compression("abcdefg"), "abcdefg")
        self.assertEqual(compression("abbbcde"), "abbbcde")
        self.assertEqual(compression("abb"), "abb")
        self.assertEqual(compression("aabcccccaaa"), "a2b1c5a3")