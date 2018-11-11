from wallaby import *
import servo as s
import motors as m
import actions as a
import constants as c
import camera as cc

def grabCan():

    s.servoInit()
    s.moveServo(c.horizontalServo, c.clawOpen, 10)
    m.driveTime(100, 100, 120)
    s.moveServo(c.horizontalServo, c.clawClose, 8)
    s.moveServo(c.verticalServo, c.armHigh, 8)
    # m.driveTime(100, 100, 2000)
    # m.driveTime(100,0,1200)
    # m.driveTime(100, 100, 2000)
    # s.moveServo(c.verticalServo, c.armMiddle, 5)
    # msleep(500)
    # s.moveServo(c.horizontalServo, c.clawOpen, 5)
    # m.drivTime(-100,0,500)
    # m.driveTime(-100, -100, 1000)


def debug():
    print "debug"
    while not left_button():
        pass


def canLineFollow():
    enable_servos()
    set_servo_position(c.horizontalServo, c.clawMiddle)
    set_servo_position(c.verticalServo, c.armHigh)
    while analog(c.etPort)<=2700:
        if analog(c.tophatPort)< 1000:
            motor(c.lMotorPort, 50)
            motor(c.rMotorPort, 0)
        else:
            motor(c.lMotorPort, 0)
            motor(c.rMotorPort, 50)
    if analog(c.etPort)>2700:
        ao()
        msleep(1000)
        a.grabCan()
        m.lineFollow()


def circle():
    m.driveTime(0,100,9000)
    m.driveTime(100,0,9000)


def square():

    m.driveTime(100, 100, 9000)

    motor(0, 100)
    motor(3, 100)
    msleep(2000)
    ao()
    motor(0, 0)
    motor(3, 100)
    msleep(1500)
    ao()

    motor(0, 100)
    motor(3, 100)
    msleep(2000)
    ao()
    motor(0, 0)
    motor(3, 100)
    msleep(1500)
    ao()

    motor(0, 100)
    motor(3, 100)
    msleep(2000)
    ao()
    motor(0, 0)
    motor(3, 100)
    msleep(1500)
    ao()

    motor(0, 100)
    motor(3, 100)
    msleep(2000)
    ao()
    motor(0, 0)
    motor(3, 100)
    msleep(1500)
    ao()

    m.driveTime(0, 100, 1500)