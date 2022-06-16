class Table:
    def __init__(self, length=5, width=5):
        self._length = length
        self._width = width

        self._grid = [[-1 for x in range(self._width)] for y in range(self._length)]

    def __str__(self):
        return self._grid

    def display(self):
        for y in range(self._length):
            print(self._grid[y])

    def put(self, x, y, entity):
        self._grid[y][x] = entity