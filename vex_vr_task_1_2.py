#region VEXcode Generated Robot Configuration
import math
import random
from vexcode import *

drivetrain = Drivetrain()
magnet = Electromagnet("magnet", 0)
pen = Pen()
brain = Brain()
left_bumper = Bumper("leftBumper", 1)
right_bumper = Bumper("rightBumper", 2)
distance = Distance()
front_eye = EyeSensor("fronteye", 3)
down_eye = EyeSensor("downeye", 4)
location = Location()

#endregion VEXcode Generated Robot Configuration
# Library imports
from vexcode import *
from math import *
from random import randint


drivetrain = Drivetrain()
magnet = Electromagnet("magnet", 0)
pen = Pen()
brain = Brain()
left_bumper = Bumper("leftBumper", 1)
right_bumper = Bumper("rightBumper", 2)
distance = Distance()
front_eye = EyeSensor("fronteye", 3)
down_eye = EyeSensor("downeye", 4)
location = Location()


def driveXDistance(setpoint,duration):
    # reset the timer
    brain.timer_reset()

    # loop while the timer is less than the duration input of the function.
    while(brain.timer_time(SECONDS)<duration):
        # Your code goes here!
        k = 2
        position = location.position(X, MM)
        error = setpoint - position
        output = k*error 
        
        drivetrain.set_drive_velocity(output, PERCENT)

        if (position < setpoint):
            drivetrain.drive(FORWARD)

        elif (position > setpoint):
            drivetrain.drive(REVERSE)

        else:
            drivetrain.stop ()


        #VEXCode VR requires that we have a small pause in any loop we run.    
        wait(1,MSEC)
    

def driveYDistance(setpoint,duration):
    # reset the timer
    brain.timer_reset()

    # loop while the timer is less than the duration input of the function.
    while(brain.timer_time(SECONDS)<duration):
        # Your code goes here!
        k = 2
        positionY = location.position(Y, MM)
        error = setpoint - positionY
        output = k*error 
        
        drivetrain.set_drive_velocity(output, PERCENT)

        if (positionY < setpoint):
            drivetrain.drive(FORWARD)

        elif (positionY > setpoint):
            drivetrain.drive(REVERSE)

        else:
            drivetrain.stop ()




        #VEXCode VR requires that we have a small pause in any loop we run.    
        wait(1,MSEC)
   

def driveDiagonalDistance(setpoint,duration):
    # reset the timer
    brain.timer_reset()

    # loop while the timer is less than the duration input of the function.
    while(brain.timer_time(SECONDS)<duration):
        # Your code goes here!
        k = 2
        positionDiag = location.position(Y, MM)
        error = setpoint - positionDiag
        output = k*error 
        
        drivetrain.set_drive_velocity(output, PERCENT)

        if (positionDiag < setpoint):
            drivetrain.drive(FORWARD)

        elif (positionDiag > setpoint):
            drivetrain.drive(REVERSE)

        else:
            drivetrain.stop ()




        #VEXCode VR requires that we have a small pause in any loop we run.    
        wait(1,MSEC)
   

# Add project code in "main"
def main():
    pen.move(DOWN)
    drivetrain.turn_to_heading(90,DEGREES,wait=True)
    driveXDistance(0,4)
    drivetrain.turn_to_heading(0,DEGREES,wait=True)
    driveYDistance(0,3)
    drivetrain.turn_to_heading(45,DEGREES,wait=True)
    driveDiagonalDistance(400,4)
# VR threads — Do not delete
vr_thread(main())

        
