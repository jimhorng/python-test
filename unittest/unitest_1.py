'''
Created on Jan 29, 2015

@author: jimhorng
'''
import unittest


class Test(unittest.TestCase):


    def testName(self):
        self.assertTrue(1)


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()