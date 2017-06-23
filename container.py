from weight_check import WeightCheck
from word_extractor import WordExtractor

class Container:

    def __init__(self, max_weight):
        self._max_weight = max_weight
        self._total_weight = 0
        self._things = []


    def total_weight(self):
        return self._total_weight


    def max_weight(self):
        return self._max_weight


    def add_suitecase(self, suitecase):
        if WeightCheck.check_invalid_add(self, suitecase):
            return

        self._total_weight += suitecase.get_weight()
        self._things.append(suitecase)


    def to_string(self):
        total_things = len(self._things)
        word = WordExtractor.get_things_word("suitecase", "suitecases", total_things)

        return "{} ({}kg)".format(word, self._total_weight)

