import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
buz_state = False
buzStart = 23
buzStop = 24
Frq = [262, 294, 330, 349, 392, 440, 492, 523]
spd = 0.5

GPIO.setup(18, GPIO.OUT) #18pin - buz power output
GPIO.setup(buzStart, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) #23pin - buz ON
GPIO.setup(buzStop, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) #buz OFF
p = GPIO.PWM(18,100)


def btn_sing(channel):
	print("btn_sing 함수 진입")
	global buz_state
	p.start(10) #PWM start
	buz_state = True
		
GPIO.add_event_detect(buzStart, GPIO.RISING, callback=btn_sing, bouncetime=300)


def btn_stop(channel):
	print("btn_stop 함수 진입")
	global buz_state
	buz_state = False
	p.stop()

GPIO.add_event_detect(buzStop, GPIO.RISING, callback=btn_stop, bouncetime=300)

try:
	while 1:
			while buz_state:
				for fr in Frq:
					p.ChangeFrequency(fr)
					time.sleep(spd)
	pass
except KeyboardInterrupt:
	p.stop()
	GPIO.cleanup()
