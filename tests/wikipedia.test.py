import unittest
import io
import sys
import os
"""
    Set the path to the src folder and import Bot class
"""
cur_path=os.path.abspath(os.path.dirname(__file__))
sys.path.insert(0, cur_path+"/..")
from src.services.wikipedia import Wikipedia

class Test(unittest.TestCase):
    myStdOut = None

    def setUp(self):
        self.myStdOut = io.StringIO()  # Create StringIO object
        sys.stdout = self.myStdOut     # and redirect stdout.
    
    """
        Test the getResponse method with an invalid query
    """
    def testGetResponseWithEmptyQuery(self):
        wikipedia = Wikipedia()
        self.assertEqual(wikipedia.getResponse(""), None)
    
    """
        Test the getResponse method with a valid query
    """
    def testGetResponseWithValidQuery(self):
        wikipedia = Wikipedia()
        self.assertNotEqual(wikipedia.getResponse("test"), "test")

    """
        Method to close the input and output stream
    """
    def tearDown(self):
        sys.stdout = sys.__stdout__   
        sys.stdin = sys.__stdin__

# Call the test class
if __name__ == '__main__':
    unittest.main()

