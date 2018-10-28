from wallaby import *
import servo as s
import motors as m
import actions as a
import constants as c

def grabCan():


    s.moveServo(c.horizontalServo, c.Open, 10)
    m.drive(100, 100, 120)
    s.moveServo(c.horizontalServo, c.Close, 8)
    s.moveServo(c.verticalServo, c.high, 8)
    m.drive(100, 100, 2000)
    m.drive(100,0,1200)
    m.drive(100, 100, 2000)
    s.moveServo(c.verticalServo, c.middle, 5)
    msleep(500)
    s.moveServo(c.horizontalServo, c.Open, 5)
    debug()
    m.drive(-100,0,500)
    m.drive(-100, -100, 1000)

def debug():
    print "debug"
    while not left_button():
        pass


def square():
    m.drive(100, 100, 9000)

    motor (0, 100)
    motor (3, 100)
    msleep (2000)
    ao()
    motor (0, 0)
    motor (3, 100)
    msleep (1500)
    ao()

    motor(0, 100)
    motor(3, 100)
    msleep(2000)
    ao()
    motor(0, 0)
    motor(3, 100)
    msleep(1500)
    ao()

    motor (0, 100)
    motor (3, 100)
    msleep (2000)
    ao()
    motor (0, 0)
    motor (3, 100)
    msleep (1500)
    ao()

    motor(0, 100)
    motor(3, 100)
    msleep(2000)
    ao()
    motor(0, 0)
    motor(3, 100)
    msleep(1500)
    ao()

    m.drive (0, 100, 1500)

