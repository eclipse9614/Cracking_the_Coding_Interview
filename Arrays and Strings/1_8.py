import unittest


def _substring(sub, origin):
    return sub in origin


def isRotation(s1, s2):
    if len(s1) != len(s2):
        return False
    return _substring(s1, s2 + s2)


class Test(unittest.TestCase):
    def test(self):
        # true cases
        self.assertTrue(isRotation("a", "a"))
        self.assertTrue(isRotation("ba", "ab"))
        self.assertTrue(isRotation("ab", "ba"))
        self.assertTrue(isRotation("cab", "abc"))
        self.assertTrue(isRotation("abc", "cab"))
        self.assertTrue(isRotation("bca", "abc"))
        self.assertTrue(isRotation("abc", "bca"))
        self.assertTrue(isRotation("2341", "1234"))
        self.assertTrue(isRotation("1234", "2341"))
        self.assertTrue(isRotation("3412", "1234"))
        self.assertTrue(isRotation("1234", "3412"))
        self.assertTrue(isRotation("4123", "1234"))
        self.assertTrue(isRotation("1234", "4123"))
        # false cases
        self.assertFalse(isRotation("123", "321"))
        self.assertFalse(isRotation("231", "321"))
        self.assertFalse(isRotation("312", "321"))
        self.assertFalse(isRotation("31", "321"))
        self.assertFalse(isRotation("21", "321"))
        self.assertFalse(isRotation("32", "321"))
        self.assertFalse(isRotation("3", "321"))
        self.assertFalse(isRotation("2", "321"))
        self.assertFalse(isRotation("1", "321"))
