import time
import can_bus
import backup_camera
import neopixel_status

backup_camera.setup()
neopixel_status.setup()
can_bus.setup()

sleep_time = 0.01

while True:
	can_bus.receive()
	if can_bus.gear_is_reverse and not backup_camera.is_enabled:
		backup_camera.enable()
		neopixel_status.reversing()
	elif backup_camera.is_enabled and not can_bus.gear_is_reverse:
		backup_camera.disable()
		neopixel_status.standby()
	time.sleep(sleep_time)
	pass
