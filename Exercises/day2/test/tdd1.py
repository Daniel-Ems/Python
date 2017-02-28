#!/usr/bin/env python3
import unittest
from Python.Exercises.day2.day2 import my_max

class TestFunction(unittest.TestCase):

    def test_max(self):
        my_max(1,2)

if __name__ == "__main__":
    unittest.main()
