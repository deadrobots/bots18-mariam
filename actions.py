from wallaby import *
import servo as s
import motors as m
import actions as a
import constants as c
import camera as cc
import utilities as u


def grabCan():

    s.servoInit()
    s.moveServo(c.horizontalServo, c.clawOpen, 8)
    msleep(50)
    s.moveServo(c.horizontalServo, c.clawClose, 8)
    msleep(50)
    s.moveServo(c.verticalServo, c.armHigh, 8)
    msleep(50)


def dropCan():
    s.moveServo(c.verticalServo, c.armMiddle, 5)
    msleep(500)
    s.moveServo(c.horizontalServo, c.clawOpen, 5)


def locateCan():

    m.drive(30,30)
    while analog_et(c.etPort) < 2900:
        msleep(20)
        print analog_et(c.etPort)
    ao()
    msleep(500)


def driveToBump():
    m.drive(20, 20)
    yTarget = 25
    while gyro_y() < yTarget:
        print gyro_y()
    ao()


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
    m.driveTime(0,100,900)
    m.driveTime(100,0,900)


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