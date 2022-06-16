from src.constants.orientation import Orientation

class Robot:
    def __init__(self, x=0, y=0, orientation=Orientation.NORTH):
        self.place(x, y, orientation)

    def __str__(self):
        val = 'R'
        if Orientation.NORTH:
            val += ' ^'
        elif Orientation.SOUTH:
            val += ' v'
        elif Orientation.WEST:
            val += ' <'
        elif Orientation.EAST:
            val += ' >'

        return val

    def __repr__(self):
        return str(self)

    def coords(self):
        return self._x, self._y

    def place(self, x, y, orientation):
        self._x = x
        self._y = y
        self._orientation = orientation

    def report(self):
        return (self._x, self._y, self._orientation)

    def move(self):
        if self._orientation == Orientation.NORTH:
            self._y += 1
        elif self._orientation == Orientation.SOUTH:
            self._y -= 1
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