
import time

import subprocess
import bitstring
# from bitstring import BitArray

def read_accel_x():
	with open("/sys/bus/iio/devices/iio:device0/in_accel_x_raw","r") as accel_x:
		#x = BitArray(accel_x.read())
		# sint = x.int
		x = int(accel_x.read())
		x = bitstring.Bits(uint=x,length=16)
		[x] = x.unpack('int')

	return (x)

def read_accel_y():
	with open("/sys/bus/iio/devices/iio:device0/in_accel_y_raw","r") as accel_y:
		y  = int(accel_y.read())
		y = bitstring.Bits(uint=y,length=16)
		[y] = y.unpack('int')

	return y


def read_accel_z():
	with open("/sys/bus/iio/devices/iio:device0/in_accel_z_raw","r") as accel_z:
		z  = int(accel_z.read())
		z = bitstring.Bits(uint=z,length=16)
		[z] = z.unpack('int')

	return z

while True:

	print "%s : %s : %s" %(read_accel_x(),read_accel_y(),read_accel_z())
	if read_accel_x > 200:

		subprocess.call(['xrandr','--output', 'eDP1', '--rotate', 'right'])

	elif read_accel_x <-200:
		subprocess.call(['xrandr','--output', 'eDP1', '--rotate', 'left'])
	time.sleep(1)

