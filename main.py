#!/usr/bin/python
import os, sys
from wallaby import *
import Servo as s

rMotorPort=0
lMotorPort=3

def drive(leftSpeed, rightSpeed, time):
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