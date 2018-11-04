#!/usr/bin/python
import os, sys
from wallaby import *
import servo as s
import motors as m
import actions as a
import constants as c


#To Do:
    #Line follow until robot detects a soda can and pick it up
    #Camera code

def main():
    a.canLineFollow()


if __name__ == "__main__":
    sys.stdout = os.fdopen(sys.stdout.fileno(), "w", 0)
    main()
