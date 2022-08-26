import unittest
from Fuction import doing_stuff


class TestFunction(unittest. TestCase):
    def test_function(self):
        self.assertAlmostEqual(doing_stuff(3, 5, 7), 17.25)
