#!/usr/bin/python
import os, sys
from wallaby import *
import servo as s
import motors as m
import actions as a
import constants as c
import camera as cc

# To Do:

    #Implement serovos with camera code
    #Bumpy

def main():
    cc.cameraInit()
    cc.locateObject2(50,60)
    print "press l button"
    while not left_button():
        pass
    cc.locateObject2(20, 80)


if __name__ == "__main__":
    sys.stdout = os.fdopen(sys.stdout.fileno(), "w", 0)
    main()
