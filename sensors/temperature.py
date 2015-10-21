# we had the data pin hooked up to pin 7 (BCM4)

import os
import glob
import time
from util.simpleMovingAverage import SimpleMovingAverage as Average
 
#os.system('modprobe w1-gpio')
#os.system('modprobe w1-therm')
 


def parse_temperature(line):
	equals_pos = line.find('t=')
	if equals_pos != -1:
		temp_string = line[equals_pos+2:]
		temp_c = float(temp_string) / 1000.0
		temp_f = temp_c * 9.0 / 5.0 + 32.0
		return temp_c, temp_f

	
def read_raw_temp(device_file):
	temperature = '----'
	f = open(device_file, 'r')
	lines = f.readlines()
	crc_line = lines[0].strip()
	temperature_line = lines[1].strip()
	f.close()
	if crc_line[-3:] =="YES":
		temperature = parse_temperature(temperature_line)

	return temperature

def read_temp():
	base_dir = '/sys/bus/w1/devices/'
	device_folders = glob.glob(base_dir + '28*')
 
	for device_folder in device_folders:
		device_file = device_folder + '/w1_slave'
		#print "--->"+device_file
		#device_file = os.path.join(dir,"temperature")
		print "{:.1f}".format(read_raw_temp(device_file)[0])


try:
    while True:
        #print(read_temp())
        read_temp()
        time.sleep(1)

except KeyboardInterrupt:
    print "exiting..."

