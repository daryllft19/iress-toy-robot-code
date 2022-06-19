class Table:
    def __init__(self, length=5, width=5):
        self._length = length
        self._width = width

        self._grid = [[-1 for x in range(self._width)] for y in range(self._length)]

    def __str__(self):
        return self._grid

    def dimensions(self):
        return self._length, self._width

    def display(self):
        for y in range(self._length):
            print('\t'.join(map(lambda x: str('_' if x == -1 else x), self._grid[y])))

    def get(self, x, y):
        row = self._length - y - 1
        column = x

        if 0 <= row <= self._length - 1 and 0 <= column <= self._width - 1:
            return self._grid[self._length - y - 1][x]
        else:
            pass
            # raise IndexError('Out of bounds')

    def set(self, x, y, entity):
        row = self._length - y - 1
        column = x

        if 0 <= row <= self._length - 1 and 0 <= column <= self._width - 1:
            self._grid[row][column] = entity
        else:
            pass
            # raise IndexError('Out of bounds')