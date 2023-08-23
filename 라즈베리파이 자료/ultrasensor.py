import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

TRIG = 23	#Trig pin : 23
ECHO = 24	#Echo pin : 24
VCC = 14  #VCC pin 14
WARN = 21 #warning output

GPIO.setup(VCC, GPIO.OUT)
GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)
GPIO.setup(WARN, GPIO.OUT)

GPIO.output(VCC, True)
#Trig핀의 신호를 0으로 출력
GPIO.output(TRIG, False)
print("Waiting for sensor to settle")
time.sleep(1)

try:
	while True:
		GPIO.output(TRIG, True)
		time.sleep(0.00001)
		GPIO.output(TRIG, False)

		while GPIO.input(ECHO)==0:
			start = time.time()
		while GPIO.input(ECHO)==1:
			stop = time.time()
		check_time = stop - start
		distance = check_time*34300/2
		print("Distance : %.1f cm" % distance)
		time.sleep(0.4)

		if distance > 10 and distance < 15:
			GPIO.output(WARN, True)
			time.sleep(1)
			GPIO.output(WARN, False)
		elif distance > 5 and distance <= 10:
			GPIO.output(WARN, True)
			time.sleep(0.6)
			GPIO.output(WARN, False)
		elif distance > 2 and distance <= 5:
			GPIO.output(WARN, True)
			time.sleep(0.3)
			GPIO.output(WARN, False)

except KeyboardInterrupt:
	print("Mesaurement stopped by User")
	GPIO.cleanup()


