import RPi.GPIO as GPIO
import time

ledG = 24	# BCM mode 핀번호
ledY = 23

GPIO.setmode(GPIO.BCM)

GPIO.setup(ledG, GPIO.OUT) # 출력핀으로 설정.
GPIO.setup(ledY, GPIO.OUT)

try:
	while True:
		GPIO.output(ledG, True)
		GPIO.output(ledY, False)
		time.sleep(0.5)
		GPIO.output(ledG, False)
		GPIO.output(ledY, True)
		time.sleep(0.5)
except KeyboardInterrupt:
	GPIO.cleanup()
