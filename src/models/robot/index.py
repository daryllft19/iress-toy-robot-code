from constants.orientation import Orientation

class Robot:
    def __init__(self, x, y, orientation):
        self.place(x, y, orientation)

    def place(self, x, y, orientation):
        self._x = x
        self._y = y
        self._orientation = orientation

    def report(self):
        return (self._x, self._y, self._orientation)

    def move(self):
        if self._orientation == Orientation.NORTH:
            self._y -= 1
        elif self._orientation == Orientation.SOUTH:
            self._y += 1
        elif self._orientation == Orientation.WEST:
            self._x -= 1
        elif self._orientation == Orientation.EAST:
            self._x += 1

    def left(self):
        if self._orientation == Orientation.NORTH:
            self._orientation = Orientation.WEST
        elif self._orientation == Orientation.SOUTH:
            self._orientation = Orientation.EAST
        elif self._orientation == Orientation.WEST:
            self._orientation = Orientation.SOUTH
        elif self._orientation == Orientation.EAST:
            self._orientation = Orientation.NORTH

    def right(self):
        if self._orientation == Orientation.NORTH:
            self._orientation = Orientation.EAST
        elif self._orientation == Orientation.SOUTH:
            self._orientation = Orientation.WEST
        elif self._orientation == Orientation.WEST:
            self._orientation = Orientation.NORTH
        elif self._orientation == Orientation.EAST:
            self._orientation = Orientation.SOUTH