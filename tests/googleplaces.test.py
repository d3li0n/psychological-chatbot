import unittest
import io
import sys
import os
"""
    Set the path to the src folder and import Bot class
"""
cur_path=os.path.abspath(os.path.dirname(__file__))
sys.path.insert(0, cur_path+"/..")
from src.services.googleplaces import GooglePlaces


class Test(unittest.TestCase):
    myStdOut = None

    def setUp(self):
        self.myStdOut = io.StringIO()  # Create StringIO object
        sys.stdout = self.myStdOut     # and redirect stdout.

    """
       Method asserts that with an empty argument provided to the constructor the error is thrown
    """
    def testEmptyBotConstructor(self):
        with self.assertRaises(TypeError) as ex:
            GooglePlaces()
            self.assertEqual(ex.exception, "Error")

    """
        Method asserts that with an invalud path and file provided, the program will exit
    """
    def testEmptyConfigPathToConstructor(self):
        with self.assertRaises(SystemExit) as ex:
            GooglePlaces("data/config.json")
            self.assertEqual(ex.exception, "Error")

    """
        Method asserts that with a valid path and file provided, API key's will not be zero
    """
    def testValidConfigPathToConstructor(self):
        serviceAPIKeyLength = len(GooglePlaces("config.json").getAPIKey())
        self.assertNotEqual(serviceAPIKeyLength, 0)

    """
        Method to close the input and output stream
    """
    def tearDown(self):
        sys.stdout = sys.__stdout__   
        sys.stdin = sys.__stdin__
# Call the test class
if __name__ == '__main__':
    unittest.main()
