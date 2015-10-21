# ------------------ HC-SR04 ----------------------
# Trigger Input Pulse with: 10uS
# Ranging Distance: 2cm - 400cm or 1 inch - 13ft 
# Resolution: 0.3cm
# Max Echo Time: 38ms if no obstacle
# Cycle Period: no less than 50ms
# -------------------------------------------------

import time
import RPi.GPIO as GPIO
from util.simpleMovingAverage import SimpleMovingAverage as Average

GPIO.setwarnings(False)

#Create Variables
delay = 0.2
trigger_delay = 0.00001
precision = 0.3

# GPIO (BCM) numbering scheme
#GPIO.setmode(GPIO.BCM)
#trigger = 12
#echo = 13

# BOARD numbering scheme
GPIO.setmode(GPIO.BOARD)
trigger = 32
echo = 33

#Setup GPIO pins
GPIO.setup(trigger, GPIO.OUT)
GPIO.setup(echo, GPIO.IN)

def ping():
    distance = 0
    ping_send = 0
    ping_return = 0
    time.sleep(0.05)
    GPIO.output(trigger, True)
    time.sleep(trigger_delay)

    GPIO.output(trigger, False)
    while GPIO.input(echo) == 0:
      ping_send = time.time()

    while GPIO.input(echo) == 1:
      ping_return = time.time()

    ping_time = ping_return - ping_send
    distance = ping_time * 17000
    return distance


print ("---- sonar ----")
try:
    while True:
        raw_distance = ping()
        distance = round(raw_distance/precision) * precision
        print "range: {0:4.1f}".format(distance)
        time.sleep(0.25)

except KeyboardInterrupt:
    print "exiting..."
    GPIO.cleanup()


