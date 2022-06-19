from src.models.robot import Robot
from src.constants.orientation import Orientation

def test_create_default_robot():
    robot = Robot()
    assert robot._x == 0
    assert robot._y == 0
    assert robot._orientation == Orientation.NORTH.name


def test_create_robot_with_x_2_y_5_facing_south():
    robot = Robot(2, 5, 'SOUTH')
    assert robot._x == 2
    assert robot._y == 5
    assert robot._orientation == Orientation.SOUTH.name

def test_robot_report():
    robot = Robot()
    assert robot.report() == (0, 0, Orientation.NORTH.name)

def test_robot_move():
    robot = Robot()
    robot.move()
    assert robot.report() == (0, 1, Orientation.NORTH.name)

def test_robot_left():
    robot = Robot()
    robot.left()
    assert robot.report() == (0, 0, Orientation.WEST.name)

def test_robot_right():
    robot = Robot()
    robot.right()
    assert robot.report() == (0, 0, Orientation.EAST.name)