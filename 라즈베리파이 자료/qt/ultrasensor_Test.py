import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

TRIG = 23
ECHO = 20

GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)

print("start after 1 second")
GPIO.output(TRIG, False)
time.sleep(1)

try:
	while True:
		GPIO.output(TRIG, True)
		time.sleep(0.00001)
		GPIO.output(TRIG, False)

		while GPIO.input(ECHO) == 0:
			start = time.time()
			#print("A")
		while GPIO.input(ECHO) == 1:
			stop = time.time()
			#print("B")

		check_time = stop-start
		distance = 34300 * check_time / 2
		print("Distance : %.1f cm" % distance)
		time.sleep(0.4)

except KeyboardInterrupt:
	print("Stopped by User")
	GPIO.cleanup()
