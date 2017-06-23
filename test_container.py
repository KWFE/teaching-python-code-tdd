import unittest
from suitecase import Suitecase
from container import Container
from thing import Thing

class TestContainer(unittest.TestCase):

    def test_add_suitecase(self):
        t = Thing("some name", 10)
        s = Suitecase(100)
        s.add_thing(t)

        c = Container(100)
        c.add_suitecase(s)

        self.assertEqual("1 suitecase (10kg)", c.to_string())

