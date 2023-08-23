import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

GPIO.setup(18, GPIO.OUT)

#PWM 인스턴스 p를 만들고 GPIO 18번을 PWM 핀으로 설정. 주파수 = 100Hz
p = GPIO.PWM(18, 100)
Frq = [262, 294, 330, 349, 392, 440, 493, 523]
speed = 0.5	#음과 음 사이 연주시간(0.5초)

p.start(10) # PWM시작. 듀티사이클10(충분)

try:
	while True:
		for fr in Frq:
			p.ChangeFrequency(fr) #주파수를 fr로 변경
			time.sleep(speed)     #speed 초만큼 딜레이
except KeyboardInterrupt:
	pass
p.stop()
GPIO.Cleanup()
