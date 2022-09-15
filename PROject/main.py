#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile



# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.


# Create your objects here.
ev3 = EV3Brick()
left_motor = Motor(Port.A, positive_direction=Direction.CLOCKWISE)
right_motor = Motor(Port.B, positive_direction=Direction.CLOCKWISE) 
both_motors = DriveBase(left_motor, right_motor, wheel_diameter=55.5, axle_track=104)

# Write your program here.
ev3.speaker.beep()
def move_forward1():
    both_motors.settings(2000, 2000, 90, 90)
    both_motors.straight(1800)
    both_motors.turn(105)
    both_motors.straight(2765)
    both_motors.turn(105)
    both_motors.straight(1800)
    both_motors.turn(105)
    both_motors.straight(800)
    both_motors.turn(315)
    both_motors.straight(500)
    both_motors.turn(105)
    both_motors.straight(2000)
    both_motors.turn(105)
    both_motors.straight(600)
def turn():
    both_motors.settings(2000, 2000, 90, 90)
    both_motors.turn(105)

# turn()
move_forward1()
# This should finish the course from Tuesday.