from wallaby import *
import servo as s
import motors as m
import actions as a
import constants as c
import camera as cc


def cameraInit():
    camera_open()


def locateObject(speed,yTarget,width):
    yPosition = 0
    center = 80
    while yPosition < yTarget:
        [xPosition, yPosition] = xCenter()
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
    camera_update()
    msleep(20)
    if get_object_count(0) == 0:  # no red objects
        xPosition = -1
        yPosition = -1
    else:  # sees red objects
        xPosition = get_object_center_x(0, 0)
        yPosition = get_object_center_y(0, 0)
    print xPosition, yPosition
    return xPosition, yPosition
