#!/usr/bin/env pybricks-micropython
from re import T
from turtle import color
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
AARCH64 = Motor(Port.C, positive_direction=Direction.CLOCKWISE)

# Write your program here.
ev3.speaker.beep()
def forward(a):
    both_motors.settings(2000, 2000, 360, 360)
    both_motors.straight(a)
def turn(b):
    both_motors.settings(2000, 2000, 360, 360)
    both_motors.turn(b)
def AARCH64():
    AARCH64.settings(2000, 2000, 360, 360)
    AARCH64.turn(180)
forward(292.1)
turn(55)
forward(101.6)
turn(-55)
forward(101.6*2)
turn(55)
forward(101.6)
turn(-55)
forward(812.8)
turn(105)
forward(635)
turn(105)
forward(812.8)
turn(105)
forward(101.6)
AARCH64()
forward(304.8)
turn(-105)
forward(101.6)
turn(55)
forward(101.6*2)
turn(-55)
forward(101.6)
turn(55)
forward(292.1)



# This should finish the course from Tuesday.
#Hi I cloned the repo -Aditya