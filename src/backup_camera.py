import digitalio
import board

camera_enable_gpio = None
is_enabled = False

def setup():
	global camera_enable_gpio
	camera_enable_gpio = digitalio.DigitalInOut(board.A2)
	camera_enable_gpio.switch_to_output(False)

def enable():
	global camera_enable_gpio
	is_enabled = value
	camera_enable_gpio.switch_to_output(True)

def disable():
	global camera_enable_gpio
	is_enabled = value
	camera_enable_gpio.switch_to_output(False)
