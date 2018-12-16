#!/usr/bin/python
import os, sys
from wallaby import *
import servo as s
import motors as m
import actions as a
import constants as c
import camera as cc
import utilities as u


def main():

    cc.cameraInit()
    s.servoInit()
    cc.locateObject2(40, 50)
    u.waitL()
    cc.locateObject2(20, 80)
    u.waitL()
    a.locateCan()
    u.waitL()
    a.grabCan()
    u.waitL()
    a.driveToBump()
    u.waitL()
    a.dropCan()


if __name__ == "__main__":
    sys.stdout = os.fdopen(sys.stdout.fileno(), "w", 0)
    main()
