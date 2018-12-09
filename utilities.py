from wallaby import *
import servo as s
import motors as m
import actions as a
import constants as c
import camera as cc
import utilities as u

def wait():
    print "press l button"
    while not left_button():
        pass


def debug():
    print "debug"
    while not left_button():
        pass