class StringBuilder(object):
    def __init__(self):
        self._array = []

    def add_word(self, word):
        for cha in word:
            self._array.append(cha)

    def to_str(self):
        return ''.join(self._array)
