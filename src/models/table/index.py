class Table:
    def __init__(self, length=5, width=5):
        self._length = length
        self._width = width

        self._grid = [[-1 for x in range(self._width)] for y in range(self._length)]

    def __str__(self):
        return self._grid

    def display(self):
        for y in range(self._length):
            print('\t'.join(map(lambda x: str('_' if x == -1 else x), self._grid[y])))

    def get(self, x, y):
        return self._grid[y][x]

    def set(self, x, y, entity):
        self._grid[y][x] = entity