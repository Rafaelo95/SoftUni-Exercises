class DictionaryIter:
    def __init__(self, dictionary_object):
        self.dictionary_object = dictionary_object
        self.k_and_v = self.dictionary_object.items()
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.dictionary_object):
            self.index += 1
            return tuple(self.k_and_v)[self.index - 1]
        raise StopIteration


result = DictionaryIter({1: "1", 2: "2"})
for x in result:
    print(x)
