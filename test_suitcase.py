import unittest
from suitecase import Suitecase
from thing import Thing

class TestSuitecase(unittest.TestCase):

    def test_add_thing(self):
        t = Thing("some name", 10)
        s = Suitecase(100)

        s.add_thing(t)

        self.assertEqual("1 thing (10kg)", s.to_string())


    def test_add_things(self):
        t = Thing("some name", 10)
        s = Suitecase(100)

        s.add_thing(t)
        s.add_thing(t)

        self.assertEqual("2 things (20kg)", s.to_string())


    def test_empty_suitecase(self):
        s = Suitecase(100)
        self.assertEqual("empty (0kg)", s.to_string())


    def test_heaviest_thing(self):
        t1 = Thing("some name", 20)
        t2 = Thing("some name", 30)

        s = Suitecase(100)
        s.add_thing(t1)
        s.add_thing(t2)

        self.assertEqual(t2, s.heaviest_thing())

    def test_heaviest_thing_empty(self):
        s = Suitecase(100)
        self.assertEqual(None, s.heaviest_thing())

