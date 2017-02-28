#!/usr/bin/env python3
import unittest
from Python.Exercises.day2.my_max import my_max

class TestFunction(unittest.TestCase):

    def test_max(self):
        my_max(1,2)
        
    def test_return(self):
        value = my_max(1,2)
        self.assertTrue(value)

if __name__ == "__main__":
    unittest.main()
