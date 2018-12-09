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


def locateObject(speed,yTarget,width):
    camera_update()
    yPosition = 0
    center = 80
    while yPosition < yTarget:
        camera_update()
        xPosition, yPosition = xCenter()
        if xPosition == -1:  # does not see red
            m.drive(25, -25)
        elif xPosition < center - width:  # red to the left
            m.drive(speed/2, speed)
        elif xPosition > center + width:  # red to the right
            m.drive(speed, speed/2)
        else:  # red in the middle
            msleep(200) 			# Unsure of what you're going for here. is this msleep()
            m.drive(speed, speed) 	# supposed to give the camera some time to update? In which
									# case, it should not be inside this "else", but at the very
									# end of your loop. Is it here so that you drive straight
									# forward some ways before checking again? In that case, the 
									# msleep should happen AFTER the m.drive() (or not at)
									# all, because you've got an msleep() every iteration of
									# your loop already -LMB
        msleep(50)
    ao()


def xCenter():
    size = get_object_area(0, 0)
    if get_object_count(0) == 0 or size < 100:  # no red objects
        xPosition = -1
        yPosition = -1
    else:  # sees red objects
        xPosition = get_object_center_x(0, 0)
        yPosition = get_object_center_y(0, 0)
    print xPosition, yPosition, size
    return xPosition, yPosition

def locateObject2(speed,yTarget):
    camera_update()
    yPosition = 0
    while yPosition < yTarget:
        camera_update()
        xPosition, yPosition = xCenter()
        if xPosition == -1:  # does not see red
            m.drive(30, -30)
        else:
            msleep(200)
            lSpeed = (int) (-speed + 1.25 * xPosition)
            if lSpeed > speed:
                lSpeed = speed
            rSpeed = (int) (speed - 1.25 * (xPosition - 80))
            if rSpeed > speed:
                rSpeed = speed
            motor(c.lMotorPort, lSpeed)
            motor(c.rMotorPort, rSpeed)
        msleep(50)
    ao()