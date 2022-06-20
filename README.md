# Toy Robot

This is a simple implementation of the toy robot that can be placed in a table and can accept certain movement commands that will allow the robot to travel within the table bounds.

## Getting Started

### Setup your virtual environment

```bash
virtualenv -ppython3 venv
source venv/bin/activate
pip install -r etc/requirements.txt
```

### Run tests

Ensure that everything is working as expected.

```bash
python -m pytest

# TODO: integration tests
```

## How to use

### Run main runner

```bash
python main.py
```

An initial series of prompts will be shown to the user to configure the table and robot features.
```text
Table Length (Defaults to 5) >>  
Table Width (Defaults to 5) >> 
Robot's X coordinate (Defaults to 0) >> 
Robot's Y Coordinate (Defaults to 0): 
Robot Orientation (Defaults to NORTH): 
Initializing...
Table(length=5, width=5)
Robot(x=0, y=0, orientation=NORTH)
Done!
```


Run HELP to check the available commands

```text
>> HELP
Commands
1. PLACE <x:int>, <y:int>, <orientation:NORTH|SOUTH|EAST|WEST> - Places a robot in the table depending on the X and Y axes, and orientation.
2. MOVE - Moves the robot forward relative its current orientation.
3. LEFT - Makes the robot face left relative its current orientation.
4. RIGHT - Makes the robot face right relative its current orientation.
5. REPORT - Prints an output of the robot's current location and orientation.
```

Every run of any command will print a display of the robot.

```text
_       _       _       _       _
_       _       _       _       _
_       _       _       _       _
_       _       _       _       _
R ^     _       _       _       _
```

### Available actionable commands

- [PLACE](/#PLACE)
- [MOVE](/#MOVE)
- [LEFT](/#LEFT)
- [RIGHT](/#RIGHT)
- [REPORT](/#REPORT)

#### PLACE

```text
>> PLACE 2,4,SOUTH
_       _       R v     _       _
_       _       _       _       _
_       _       _       _       _
_       _       _       _       _
_       _       _       _       _
```

#### MOVE
```text
>> MOVE
_       _       _       _       _
_       _       R v     _       _
_       _       _       _       _
_       _       _       _       _
_       _       _       _       _
```

#### LEFT
```text
>> LEFT
_       _       _       _       _
_       _       R >     _       _
_       _       _       _       _
_       _       _       _       _
_       _       _       _       _
```

#### RIGHT
```text
>> RIGHT
_       _       _       _       _
_       _       R v     _       _
_       _       _       _       _
_       _       _       _       _
_       _       _       _       _
```

#### REPORT

```text
>> REPORT
>> Output: 2 3 EAST
_       _       _       _       _
_       _       R >     _       _
_       _       _       _       _
_       _       _       _       _
_       _       _       _       _
```
