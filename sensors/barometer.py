#!/usr/bin/env python

import Adafruit_BMP.BMP085 as BMP085
from util.simpleMovingAverage import SimpleMovingAverage as Average
from time import sleep
from random import uniform as rand

# import sys
# sys.path.insert(1,'/usr/local/bin')


# Sensor Modes:
# ---------------------
# BMP085_ULTRALOWPOWER
# BMP085_STANDARD
# BMP085_HIGHRES
# BMP085_ULTRAHIGHRES

edmonton_altitude = 668 # meters
# sensor = BMP085.BMP085()
# p0 = sensor.read_sealevel_pressure(edmonton_altitude)


def getReading():
	return rand(1.0,8.3)
	# return sensor.read_pressure()


# print 'Temp = {0:0.2f} *C'.format(sensor.read_temperature())
# print 'Pressure = {0:0.2f} Pa'.format(sensor.read_pressure())
# print 'Altitude = {0:0.2f} m'.format(sensor.read_altitude(p0))
# print 'Sealevel Pressure = {0:0.2f} Pa'.format(sensor.read_sealevel_pressure(edmonton_altitude))

def do_it():
    avgPressure = Average('pressure', 10)
    # while True:
    for _ in range(1,100):
        newReading = getReading()
        avgPressure.getAverage(newReading)
        # sleep(0.01)
    print "the smoothed average is %f" %  avgPressure.getAverage(newReading)


if __name__ == '__main__':
    print '---- barometer -----'
    do_it()


