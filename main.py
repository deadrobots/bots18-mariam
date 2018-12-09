#!/usr/bin/python
import os, sys
from wallaby import *
import servo as s
import motors as m
import actions as a
import constants as c
import camera as cc
import utilities as u

# To Do:

    #Implement serovos with camera code
    #Bumpy

def main():

    # cc.cameraInit()
    # s.servoInit()
    # cc.locateObject2(50, 60)
    # u.wait()
    # cc.locateObject2(20, 80)
    # u.wait()
    # a.locateCan()
    # u.wait()
    # a.grabCan()

    a.driveToBump()

if __name__ == "__main__":
    sys.stdout = os.fdopen(sys.stdout.fileno(), "w", 0)
    main()
