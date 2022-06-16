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
        return self._grid[y][x]

    def set(self, x, y, entity):
        row = self._length - y - 1
        column = x

        if 0 <= row <= self._length - 1 and 0 <= column <= self._width - 1:
            self._grid[row][column] = entity