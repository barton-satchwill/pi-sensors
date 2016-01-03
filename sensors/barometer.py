#!/usr/bin/env python

# ------------------ BMP-085 ----------------------
# Cycle Period: no less than 50ms
# Sample Rate: up to 128 times per second for standard mode
# -------------------------------------------------
#           
# sda -----------------o BCM 2 (SDA)
# scl -----------------o BCM 3 (SCL)
# vcc -----------------o 3.3V
# gnd -----------------o gnd
# -------------------------------------------------

import Adafruit_BMP.BMP085 as BMP085
from util.simpleMovingAverage import SimpleMovingAverage as Average
from time import sleep
from time import time
from datetime import datetime

# import sys
# sys.path.insert(1,'/usr/local/bin')

# Sensor Modes:
# ---------------------
# BMP085_ULTRALOWPOWER
# BMP085_STANDARD
# BMP085_HIGHRES
# BMP085_ULTRAHIGHRES

edmonton_altitude = 668 # meters
sensor = BMP085.BMP085()

def read_sealevel_pressure(pressure, altitude_m=0.0):
    """Calculates the pressure at sealevel when given a 
        known altitude in meters. Returns a value in Pascals."""
    p0 = pressure / pow(1.0 - altitude_m/44330.0, 5.255)
    return p0


def read_altitude(pressure, sealevel_pa=101325.0):
    """Calculates the altitude in meters."""
    altitude = 44330.0 * (1.0 - pow(pressure / sealevel_pa, (1.0/5.255)))
    return altitude

def get_pressure():
    avgPressure = Average('pressure', 100)
    for i in range(0,62):
        p = avgPressure.getAverage(sensor.read_pressure())
    return p

def get_temperature():
    avgTemp = Average('temperature', 60)
    for _ in range(1,60):
        t = avgTemp.getAverage(sensor.read_temperature())
    return t



def run():
    avgTemp = Average('temperature', 100)
    avgPressure = Average('pressure', 100)
    avgAlt = Average('altitude', 100)
    avgSeaLevelPressure = Average('sea level pressure', 100)

    print "Time\tTemp\tPress\tAlt\tSealevel Pressure"
    print "--------------------------------------------------"

    while True:
        for _ in range(1,60):
            t = avgTemp.getAverage(sensor.read_temperature())
            p = avgPressure.getAverage(sensor.read_pressure())
            p0 = avgSeaLevelPressure.getAverage(read_sealevel_pressure(p, edmonton_altitude))
            a = avgAlt.getAverage(read_altitude(p, p0))
            sleep(10)
        #print '             Temp = {0:0.2f} *C'.format(t)
        #print '         Pressure = {0:0.2f} kPa'.format(p/1000)
        #print '         Altitude = {0:0.2f} m'.format(a)
        #print 'Sealevel Pressure = {0:0.2f} kPa'.format(p0/1000)
        #print '--------------------------------'
        now = datetime.strftime(datetime.now(), '%Y-%m-%d %H:%M:%S')
        reading = "{0}\t{1:0.2f}\t{2:0.2f}\t{3:0.2f}\t{4:0.2f}".format(now, t, p/1000, a, p0/1000)
        log = open("pressure.csv",'a')
        print reading
        log.write(reading+"\n")
        log.close()

if __name__ == '__main__':
    print '---- barometer -----'
    # run()
    get_pressure()

