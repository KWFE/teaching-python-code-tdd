import unittest
from thing import Thing

class TestThing(unittest.TestCase):

    def test_get_name(self):
        t = Thing("some name", 10)
        self.assertEqual("some name", t.get_name())


    def test_get_weight(self):
        t = Thing("some weight", 10)
        self.assertEqual(10, t.get_weight())


    def test_to_string(self):
        t = Thing("some string", 10)
        self.assertEqual("some string (10kg)", t.to_string())
