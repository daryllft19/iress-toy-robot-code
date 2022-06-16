from src.constants.orientation import Orientation

class Robot:
    def __init__(self, x=0, y=0, orientation=Orientation.NORTH.name):
        self.place(x, y, orientation)

    def __str__(self):
        val = 'R'
        if self._orientation == Orientation.NORTH.name:
            val += ' ^'
        elif self._orientation == Orientation.SOUTH.name:
            val += ' v'
        elif self._orientation == Orientation.WEST.name:
            val += ' <'
        elif self._orientation == Orientation.EAST.name:
            val += ' >'

        return val

    def __repr__(self):
        return str(self)

    def coords(self):
        return self._x, self._y

    def orientation(self):
        return self._orientation

    def place(self, x, y, orientation):
        self._x = x
        self._y = y
        self._orientation = orientation

    def report(self):
        return (self._x, self._y, self._orientation)

    def move(self):
        if self._orientation == Orientation.NORTH.name:
            self._y += 1
        elif self._orientation == Orientation.SOUTH.name:
            self._y -= 1
        elif self._orientation == Orientation.WEST.name:
            self._x -= 1
        elif self._orientation == Orientation.EAST.name:
            self._x += 1

    def left(self):
        if self._orientation == Orientation.NORTH.name:
            self._orientation = Orientation.WEST.name
        elif self._orientation == Orientation.SOUTH.name:
            self._orientation = Orientation.EAST.name
        elif self._orientation == Orientation.WEST.name:
            self._orientation = Orientation.SOUTH.name
        elif self._orientation == Orientation.EAST.name:
            self._orientation = Orientation.NORTH.name

    def right(self):
        if self._orientation == Orientation.NORTH.name:
            self._orientation = Orientation.EAST.name
        elif self._orientation == Orientation.SOUTH.name:
            self._orientation = Orientation.WEST.name
        elif self._orientation == Orientation.WEST.name:
            self._orientation = Orientation.NORTH.name
        elif self._orientation == Orientation.EAST.name:
            self._orientation = Orientation.SOUTH.name