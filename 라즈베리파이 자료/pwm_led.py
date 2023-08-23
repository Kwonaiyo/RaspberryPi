import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

GPIO.setup(23, GPIO.OUT)
GPIO.setup(24, GPIO.OUT)
GPIO.setup(25, GPIO.OUT)

p = GPIO.PWM(23, 310)
r = GPIO.PWM(24, 310)
s = GPIO.PWM(25, 310)

p.start(0)
r.start(0)
s.start(0)

try:
	while True:
		for dc in range(0, 101, 10):
			p.ChangeDutyCycle(dc)
			r.ChangeDutyCycle(dc)
			s.ChangeDutyCycle(dc)
			time.sleep(0.1)
		for dc in range(100, -1, -10):
			p.ChangeDutyCycle(dc)
			r.ChangeDutyCycle(dc)
			s.ChangeDutyCycle(dc)
			time.sleep(0.1)
except KeyboardInterrupt:
	pass
p.stop()
r.stop()
s.stop()
GPIO.cleanup()
