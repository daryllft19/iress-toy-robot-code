from enum import Enum, auto

class Command(Enum):
    PLACE = 'PLACE'
    REPORT = 'REPORT'
    MOVE = 'MOVE'
    LEFT = 'LEFT'
    RIGHT = 'RIGHT'
    HELP = 'HELP'