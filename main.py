#!/usr/bin/python
import os, sys
from wallaby import *
import Servo as s

rMotorPort=0
lMotorPort=3

# Great job on beginning to break up your code into separate files, Mariam.
# I would suggest the following format:
# constants.py (holds your constants!)
# actions.py  (contains collections of motor and servo commands to perform an action. EX: grabCan() )
# servo.py (just holds servo related functions. Not motor commands, generally)
# motors.py (just holds your motor commands. drive(), driveTimed(), driveUntilBlackLine(), stuff like that.)
# main.py (where everything starts!)
# You're off to a great start on this.
# -LMB

def drive(leftSpeed, rightSpeed, time): # Duplicate function (found one in Servo.py) -LMB
    if rightSpeed < 0:
        rightSpeed = rightSpeed + 2
    else:
        rightSpeed = rightSpeed - 2

    motor(lMotorPort, leftSpeed)
    motor(rMotorPort, rightSpeed)
    msleep(time)
    ao()

# Creating a function for drive straight. Make Sandy drive in a square using drive function


def main():
    print "Running Code"
    s.servoinit()
   # print "Square"

   # drive(100, 100, 9000)

    # motor (0, 100)
    # motor (3, 100)
    # msleep (2000)
    # ao()
    # motor (0, 0)
    # motor (3, 100)
    # msleep (1500)
    # ao()
    #
    # motor(0, 100)
    # motor(3, 100)
    # msleep(2000)
    # ao()
    # motor(0, 0)
    # motor(3, 100)
    # msleep(1500)
    # ao()
    #
    # motor (0, 100)
    # motor (3, 100)
    # msleep (2000)
    # ao()
    # motor (0, 0)
    # motor (3, 100)
    # msleep (1500)
    # ao()
    #
    # motor(0, 100)
    # motor(3, 100)
    # msleep(2000)
    # ao()
    # motor(0, 0)
    # motor(3, 100)
    # msleep(1500)
    # ao()

    # drive (0, 100, 1500)


if __name__ == "__main__":
    sys.stdout = os.fdopen(sys.stdout.fileno(), "w", 0)
    main()