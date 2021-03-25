from rearrange import rearrange_name

import unittest

class TestRearrange(unittest.TestCase):
    def test_basic(self):
        testcase = "Dib, Tarek"
        expected = "Tarek Dib"
        self.assertEqual(rearrange_name(testcase), expected)
    
    def test_empty(self):
        testcase = ""
        expected = ""
        self.assertEqual(rearrange_name(testcase), expected)

    def test_double_name(self):
        testcase = "Dib, Tarek M."
        expected = "Tarek M. Dib"
        self.assertEqual(rearrange_name(testcase), expected)

    def test_one_name(self):
        testcase = "Tarek"
        expected = "Tarek"
        self.assertEqual(rearrange_name(testcase), expected)

unittest.main()