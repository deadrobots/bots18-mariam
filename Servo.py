from wallaby import *

rMotorPort = 0
lMotorPort = 3
verticalServo = 3
horizontalServo = 2

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

def drive(leftSpeed, rightSpeed, time):
    if rightSpeed < 0:
        rightSpeed = rightSpeed + 2
    else:
        rightSpeed = rightSpeed - 2

    motor(lMotorPort, leftSpeed)
    motor(rMotorPort, rightSpeed)
    msleep(time)
    ao()

def servoinit():
    enable_servos()
    set_servo_position(horizontalServo, 584)
    set_servo_position(verticalServo, 1509)

    set_servo_position(horizontalServo, Open)
    drive(100, 100, 150)
    msleep(1000)
    set_servo_position(horizontalServo, Close)
    msleep(500)
    set_servo_position(verticalServo, high)
    drive(100, 100, 2000)
    msleep(1000)
    set_servo_position(verticalServo, middle)
    msleep(500)
    set_servo_position(horizontalServo, Open)
    drive(-100, -100, 1000)
    msleep(1000)



