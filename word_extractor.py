class WordExtractor:

    @staticmethod
    def get_things_word(singular, plural, things_count):
        if things_count == 0:
            return "empty"

        if things_count == 1:
            return "1 {}".format(singular)

        return "{} {}".format(things_count, plural)
