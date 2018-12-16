from wallaby import *
import servo as s
import motors as m
import actions as a
import constants as c
import camera as cc
import utilities as u


def waitL():
    print "press l button"
    while not left_button():
        pass


def waitR():
    print "press r button"
    while not right_button():
        pass


def debug():
    print "debug"
    while not left_button():
        pass
