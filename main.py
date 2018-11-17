#!/usr/bin/python
import os, sys
from wallaby import *
import servo as s
import motors as m
import actions as a
import constants as c
import camera as cc

# To Do:
    #Why does robot go slow after it loses red
    #Implement serovos with camera code
    #Bumpy
	
# Perhaps the robot goes slow after it loses red because you are telling it to find
# red twice (two calls to locateObject()) and the second call has a slower drive speed -LMB

def main():
    cc.cameraInit()
    cc.locateObject(50,60, 13)
    cc.locateObject(20, 80, 3)


if __name__ == "__main__":
    sys.stdout = os.fdopen(sys.stdout.fileno(), "w", 0)
    main()
