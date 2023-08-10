#Jacob Stasiewicz Version
from time import sleep
from picamera2 import Picamera2
from picamera2 import Preview
from datetime import datetime, timedelta

now = datetime.now()
print("Worm Cam Version 0.1")
print("MIT License")
print("Creator: Samuel Stasiewicz")
print("Last Edited: 06/03/2023")

def take_picture():
	
	global now
	#photo date/time
	nowname = str(now)[0:10]
	camera = Picamera2()
	sleep(5)  # Wait for the camera to warm up
	
	camera.start()
	print("hello")
	sleep(2)
	camera.capture_file('wormcam/wormcampics' + str(nowname) + '.jpg')
	camera.close()

# Calculate the next 3:25 pm
next_capture_time = datetime(now.year, now.month, now.day, now.hour, 10)

# If the next capture time has already passed for today, move it to tomorrow
if now > next_capture_time:
    next_capture_time += timedelta(days=1)
# Calculate the time difference in seconds until the next capture
time_difference = (next_capture_time - now).total_seconds()

# Wait until the next capture time
sleep(time_difference)

# Capture the picture at the scheduled time
take_picture()

#testing to see if this worls
print("hello jacob #3")
