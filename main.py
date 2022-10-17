from logger import logger

nested_list = [
    ['a', 'b', 'c'],
    ['d', 'e', 'f', 'h', False],
    [1, 2, None],
]


class FlatIterator:
    def __init__(self, lists):
        self.lists = lists

    def __iter__(self):
        self.cursor = 0
        self.undercursor = -1
        return self

    def __next__(self):
        if self.undercursor < len(self.lists[self.cursor])-1:
            self.undercursor += 1
            return self.lists[self.cursor][self.undercursor]
        else:
            self.cursor += 1
            self.undercursor = 0
            if self.cursor == len(self.lists):
                raise StopIteration
            else:
                return self.lists[self.cursor][self.undercursor]


def flat_generator(lists):
    cursor = 0
    undercursor = 0
    while cursor < len(lists):
        while undercursor < len(lists[cursor]):
            yield lists[cursor][undercursor]
            undercursor += 1
        undercursor = 0
        cursor += 1


@logger
def flat_iterator(lists):
    for item in FlatIterator(lists):
        print(item)


@logger
def flatgenerator(lists):
    for item in flat_generator(lists):
        print(item)

@logger
def flatlist(lists):
    flat_list = [item for item in FlatIterator(lists)]
    print(flat_list)

if __name__ == "__main__":
    flat_iterator(nested_list)
    flatgenerator(nested_list)
    flatlist(nested_list)