import RPi.GPIO as GPIO
import time

sigIn = 24
ledY = 23

GPIO.setmode(GPIO.BCM)

GPIO.setup(ledY, GPIO.OUT)	#Y를 출력으로 사용
GPIO.setup(sigIn, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

light_on = False
GPIO.setwarnings(False)

try:
	while True:
		if GPIO.input(sigIn) == GPIO.HIGH:
			light_on = not light_on
		if light_on == False and GPIO.input(sigIn) == GPIO.HIGH:
			GPIO.setup(ledY, True)
			print("LED ON")
		elif light_on == True and GPIO.input(sigIn) == GPIO.HIGH:
			GPIO.setup(ledY, False)
			print("LED OFF")
		time.sleep(0.2)
except KeyboardInterrupt:
	GPIO.cleanup()
