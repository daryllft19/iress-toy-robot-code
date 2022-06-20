from src.constants.command import Command
from src.constants.orientation import Orientation
from src.models.robot import Robot
from src.models.table import Table

def initialize(robot=Robot(), table=Table()):
    x_coord, y_coord = robot.coords()
    table.set(x_coord, y_coord, robot)
    return robot, table

def is_move_valid(robot, table):
    x, y = robot.coords()
    length, width = table.dimensions()

    if  robot.orientation() == Orientation.NORTH.name and y+1 >= length or \
        robot.orientation() == Orientation.SOUTH.name and y-1 < 0 or \
        robot.orientation() == Orientation.EAST.name and x+1 >= width or \
        robot.orientation() == Orientation.WEST.name and x-1 < 0:
            return False

    return True

def move(robot, table):
    if is_move_valid(robot, table):
        x_coord, y_coord = robot.coords()
        table.set(x_coord, y_coord, -1)
        robot.move()
        x_coord, y_coord = robot.coords()
        table.set(x_coord, y_coord, robot)

def print_help():
    print("Commands")
    print("1. PLACE <x:int>, <y:int>, <orientation:NORTH|SOUTH|EAST|WEST> - Places a robot in the table depending on the X and Y axes, and orientation.")
    print("2. MOVE - Moves the robot forward relative its current orientation.")
    print("3. LEFT - Makes the robot face left relative its current orientation.")
    print("4. RIGHT - Makes the robot face right relative its current orientation.")
    print("5. REPORT - Prints an output of the robot's current location and orientation.")

if __name__ == '__main__':

    while True:
        try:
            table_length = input('Table Length (Defaults to 5) >> ')

            if not table_length:
                table_length = 5
                break
            else:
                table_length = int(table_length)
        except ValueError:
            print('Table length should be a positive integer.')
            continue

        if isinstance(table_length, int) and table_length >= 1:
            break

        print('Table width should be a positive integer.')

    while True:
        try:
            table_width = input('Table Width (Defaults to 5) >> ')
            if not table_width:
                table_width = 5
                break
            else:
                table_width = int(table_width)
        except ValueError:
            print('Table width should be a positive integer.')
            continue

        if isinstance(table_width, int) and table_width >= 1:
            break
        
        print('Table width should be a positive integer.')
    
    while True:
        try:
            robot_x = input("Robot's X coordinate (Defaults to 0) >> ")
            if not robot_x:
                robot_x = 0
                break
            else:
                robot_x = int(robot_x)
        except ValueError:
            print("Robot's X coordinate should be zero or a positive integer.")
            continue

        if isinstance(robot_x, int) and robot_x >= 0:
            break
    
        print("Robot's X coordinate should be zero or a positive integer.")
            
    while True:
        try:
            robot_y = input("Robot's Y Coordinate (Defaults to 0): ")
            if not robot_y:
                robot_y = 0
                break
            else:
                robot_y = int(robot_y)
        except ValueError:
            print("Robot's Y coordinate should be zero or a positive integer.")
            continue

        if isinstance(robot_y, int) and robot_y >= 0:
            break

        print("Robot's Y coordinate should be zero or a positive integer.")

    while True:
        robot_orientation = input('Robot Orientation (Defaults to NORTH): ')
        if not robot_orientation:
            robot_orientation = 'NORTH'

        if isinstance(robot_orientation, str) and robot_orientation in Orientation.__members__.keys():
            break

    print('Initializing...')
    print(f'Table(length={table_length}, width={table_width})')
    print(f'Robot(x={robot_x}, y={robot_y}, orientation={robot_orientation})')
    robot, table = initialize(robot=Robot(x=robot_x, y=robot_y, orientation=robot_orientation), table=Table(length=table_length, width=table_width))
    print('Done!\n')

    while True:
        command = input('>> ').split(' ')

        if len(command) == 1:
            action = command[0]
        elif len(command) == 2:
            action,parameter = command[:2]

        if action == Command.PLACE.name:
            try:
                robot_x, robot_y, robot_orientation = parameter.split(',')
                robot_x = int(robot_x)
                robot_y = int(robot_y)

                if 0 <= robot_x < table_width and 0 <= robot_y < table_length:
                    robot, table = initialize(robot=Robot(x=robot_x, y=robot_y, orientation=robot_orientation), table=Table(length=table_length, width=table_width))
            except:
                pass
        elif action == Command.REPORT.name:
            robot_x, robot_y, robot_orientation = robot.report()
            print(f'>> Output: {robot_x} {robot_y} {robot_orientation}')
        elif action == Command.MOVE.name:
            move(robot, table)
        elif action == Command.LEFT.name:
            robot.left()
        elif action == Command.RIGHT.name:
            robot.right()
        elif action == Command.HELP.name:
            print_help()
        else:
            print('Type HELP for more information')

        table.display()