# replace " " with "%20" suppose there are enough spaces in the end of string
import unittest


def replaceSpacesNative(input_str):
    # components = input_str.split()
    # return "%20".join(components)
    # the solution above will ignore leading spaces
    # we need a preprocess and postprocess
    assert input_str.strip() != ""
    input_str = "a" + input_str
    components = input_str.split()
    return "%20".join(components)[1:]  # leave out the leading "a"


def replaceSpaces(input_str):
    lastNonSpace = -1
    for i, element in enumerate(reversed(input_str)):
        if not element.isspace():
            lastNonSpace = i
            break
    # cannot be pure string with spaces
    assert lastNonSpace != -1
    # python cannot replace chars in place
    # create a new string
    res = ""
    for i, element in enumerate(input_str[-lastNonSpace - 1::-1]):
        if element.isspace():
            res += "02%"
        else:
            res += element
    return res[::-1]  # reverse


class Test(unittest.TestCase):
    def testNativeMethod(self):
        self.assertEqual(replaceSpacesNative(" Mr John Smith      "), "%20Mr%20John%20Smith")
        self.assertEqual(replaceSpacesNative("a b c    "), "a%20b%20c")
        self.assertEqual(replaceSpacesNative(" a  "), "%20a")
        self.assertRaises(AssertionError, replaceSpacesNative, " ")

    def testMethod2(self):
        self.assertEqual(replaceSpaces(" Mr John Smith      "), "%20Mr%20John%20Smith")
        self.assertEqual(replaceSpaces("a b c    "), "a%20b%20c")
        self.assertEqual(replaceSpaces(" a  "), "%20a")
        self.assertRaises(AssertionError, replaceSpaces, " ")