from wallaby import *
import servo as s
import motors as m
import actions as a
import constants as c

def drive(leftSpeed, rightSpeed, time):
    if rightSpeed < 0:
        rightSpeed = rightSpeed + 2
    else:
        rightSpeed = rightSpeed - 2

    motor(c.lMotorPort, leftSpeed)
    motor(c.rMotorPort, rightSpeed)
    msleep(time)
    ao()

def lineFollow():
    while True:
        if analog(c.tophatPort)< 1000:
            motor(c.lMotorPort, 75)
            motor(c.rMotorPort, 0)
        else:
            motor(c.lMotorPort, 0)
            motor(c.rMotorPort, 75)


