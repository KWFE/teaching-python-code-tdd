import unittest
from brick_container import BrickContainer

class TestBrickContainer(unittest.TestCase):

    def test_get_next_brick(self):
        bc = BrickContainer(1, 1000)
        self.assertEqual(1, bc.get_next_brick().get_weight())


    def test_get_next_brick_in_loop(self):
        bc = BrickContainer(1, 1000)

        for i in range(250):
            brick = bc.get_next_brick()

        self.assertEqual(100, bc.get_next_brick().get_weight())


    def test_get_next_brick_in_loop(self):
        bc = BrickContainer(1, 1000)

        bc.add_suitecases()
        self.assertEqual("44 suitecases (990kg)", bc.get_container().to_string())
