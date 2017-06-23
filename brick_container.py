from thing import Thing
from container import Container
from suitecase import Suitecase

class BrickContainer:
    def __init__(self, brick_weight, max_container_weight):
        self._container = Container(max_container_weight)
        self._brick_weight = brick_weight
        self._max_container_weight = max_container_weight


    def get_next_brick(self):
        brick = Thing("brick", self._brick_weight)

        if self._brick_weight < 100:
            self._brick_weight += 1

        return brick


    def get_container(self):
        return self._container


    def add_suitecases(self):
        for i in range(100):
            brick = self.get_next_brick()

            suitecase = Suitecase(100)
            suitecase.add_thing(brick)

            self._container.add_suitecase(suitecase)
