import unittest
from algorithms import *


class TestAlgorithms(unittest.TestCase):

    def setUp(self):
        self.unordered_list = [35.3, 54, 764.2, 40.3, 1000, -4, -20.4]
        self.expected_order = [-20.4, -4, 35.3, 40.3, 54, 764.2, 1000]

    def test_bubble_sort(self):
        """Tests bubble sort algorithm."""
        self.assertEqual(bubble_sort(self.unordered_list), self.expected_order)
