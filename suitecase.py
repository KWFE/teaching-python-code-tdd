from word_extractor import WordExtractor
from weight_check import WeightCheck

class Suitecase:
    def __init__(self, max_weight):
        self._max_weight = max_weight
        self._total_weight = 0
        self._things = []


    def total_weight(self):
        return self._total_weight


    def get_weight(self):
        return self._total_weight


    def max_weight(self):
        return self._max_weight


    def add_thing(self, thing):
        if WeightCheck.check_invalid_add(self, thing):
            return

        self._total_weight += thing.get_weight()
        self._things.append(thing)


    def total_weight(self):
        return self._total_weight


    def heaviest_thing(self):
        heaviest_thing = None

        for thing in self._things:
            if not heaviest_thing:
                heaviest_thing = thing
                continue

            if heaviest_thing.get_weight() < thing.get_weight():
                heaviest_thing = thing

        return heaviest_thing


    def to_string(self):
        total_things = len(self._things)
        word = WordExtractor.get_things_word("thing", "things", total_things)


        return "{} ({}kg)".format(word, self._total_weight)

