from wallaby import *
import servo as s
import motors as m
import actions as a
import constants as c


Open = 0		# These look like constants, and so should be in constants.py.
Close = 1167	# Careful about defining these values in two places, as that could
high = 2047		# become confusing. You might also want to give them more descriptive
middle = 1520	# names: "ClawOpen", or "ArmMiddle". Additionally, when setting servos
low = 1277		# to extreme values (0 or 2047), many servos will "stick" to their extreme
				# end-stop positions, because they are unable to reach exactly 0 or 2047.
				# Please replace these numbers with nearby values that are safer for your
				# hardware. Instead of 0, use 100. Instead of 2047, use 1900 -LMB
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

# I like this code. I think it can be re-written to only use a single While loop, but
# the ability to slowly move a servo is an important tool to have. -LMB
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