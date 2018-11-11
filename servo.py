from wallaby import *
import servo as s
import motors as m
import actions as a
import constants as c
import camera as cc


def servoInit():
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