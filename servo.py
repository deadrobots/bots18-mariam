from wallaby import *
import servo as s
import motors as m
import actions as a
import constants as c


Open = 0
Close = 1167
high = 2047
middle = 1520
low = 1277

#PORT 2
    #OPEN: 0
    #MIDDLE:584
    #CLOSED: 1167
#PORT 3
    #HIGH: 2047
    #MIDDLE:1662
    #LOW: 1277

def servoinit():
    enable_servos()
    set_servo_position(c.horizontalServo, 584)
    set_servo_position(c.verticalServo, 1509)


def moveServo (servoPort, newPosition, speed):
    currentPosition = get_servo_position(c.horizontalServo)
    if (newPosition>currentPosition):
        while currentPosition<newPosition:
            currentPosition = currentPosition + speed
            set_servo_position(servoPort,currentPosition)
            msleep(5)
        set_servo_position(servoPort, newPosition)
    else:
        while currentPosition>newPosition:
            currentPosition = currentPosition - speed
            set_servo_position(servoPort,currentPosition)
            msleep(5)
        set_servo_position(servoPort, newPosition)