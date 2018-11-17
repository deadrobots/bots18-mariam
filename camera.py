from wallaby import *
import servo as s
import motors as m
import actions as a
import constants as c
import camera as cc

"""
If your camera output is especially "jumpy" or "noisy", then consider making some code to average
out the values for the x position of the largest object.

I would suggest using a list [] to keep track of the last five frames of data (and only five frames)
and a function that returns the average value of that list.

# Try using these commands:
myList = [4, 5, 6]
myList.append(99) # or any number. Adds 99 to the list.
myList.pop(0) # returns the left-most (first) item in the list. 4, in this case. 
"""
def cameraInit():
    camera_open()

# I like the inclusion of a "width" that defines centeredness. -LMB
def locateObject(speed,yTarget,width):
    yPosition = 0
    center = 80
    while yPosition < yTarget:
        [xPosition, yPosition] = xCenter() 	# the [] square-brackets aren't needed for this to work as you're doing. Remove them -LMB
        if xPosition == -1:  # does not see red
            m.drive(30, -30)
        elif xPosition < center - width:  # red to the left
            m.drive(0, speed)
        elif xPosition > center + width:  # red to the right
            m.drive(speed, 0)
        else:  # red in the middle
            m.drive(speed, speed)
    #ao()


def xCenter():
    camera_update()	# Ideally the camera_update() command is called at the beginning of the while loop that uses
    msleep(20)		# the camera. Also the camera is only updating about every 150ms, so it makes sense to 
					# msleep() for longer than just 20ms (~10FPS camera = 100ms, but I'm pretty sure 
					# that the camera actually only gives about ~5FPS, which is a 200ms delay) -LMB
    if get_object_count(0) == 0:  # no red objects
        xPosition = -1
        yPosition = -1
    else:  # sees red objects
        xPosition = get_object_center_x(0, 0)
        yPosition = get_object_center_y(0, 0)
    print xPosition, yPosition
    return xPosition, yPosition
