#interrupt Test..
import RPi.GPIO as GPIO
import time

ledFlag = False
led = 23
sw = 24

GPIO.setmode(GPIO.BCM)
GPIO.setup(led, GPIO.OUT)
GPIO.setup(sw, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

def ledBlink(channel):
	global ledFlag
	if ledFlag == False:
		GPIO.output(led, True)
		ledFlag = True
		print("LED ON")
	else:
		GPIO.output(led, False)
		ledFlag = False
		print("LED OFF")
GPIO.add_event_detect(sw, GPIO.RISING, callback=ledBlink, bouncetime=300)

try:
	while True:
		pass
except KeyboardInterrupt:
	GPIO.cleanup()
