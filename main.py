#!/usr/bin/python
import os, sys
from wallaby import *
import servo as s
import motors as m
import actions as a
import constants as c

# Your code looks pretty good! 
# Once you accomplish line-following using the top-hat sensor,
# then move on to line-following until you detect a soda can in front
# of your robot (using the ET sensor). Pick up the can with your bot.
# After that, you'll be ready to start on camera code! -LMB
def main():
    s.servoinit()
    a.grabCan()


if __name__ == "__main__":
    sys.stdout = os.fdopen(sys.stdout.fileno(), "w", 0)
    main()