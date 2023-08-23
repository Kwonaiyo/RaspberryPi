from flask import Flask, request
from flask import render_template
import RPi.GPIO as GPIO
import time


app = Flask(__name__)

WhileFlag = False

#pin number, GPIO setting ..
GPIO.setmode(GPIO.BCM)

#GPIO 10, 9, 11 for LED
LED_A = 10
LED_B = 9
LED_C = 11
#GPIO 23, 20 for ULTRASONIC
TRIG = 23
ECHO = 20
#GPIO 17 for BUZZER
BUZZ = 17

GPIO.setup(LED_A, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(LED_B, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(LED_C, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(TRIG, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(ECHO, GPIO.IN)
GPIO.setup(BUZZ, GPIO.OUT, initial=GPIO.LOW)

@app.route("/")
def home():
	return render_template("projindex.html")

@app.route("/led/on")
def led_on():
	try:
		GPIO.output(LED_A, GPIO.HIGH)
		GPIO.output(LED_B, GPIO.HIGH)
		GPIO.output(LED_C, GPIO.HIGH)
		return "ok"
	except expression as identifier:
		return "fail"

@app.route("/led/off")
def led_off():
	try:
		GPIO.output(LED_A, GPIO.LOW)
		GPIO.output(LED_B, GPIO.LOW)
		GPIO.output(LED_C, GPIO.LOW)
		return "ok"
	except expression as identifier:
		return "fail"

@app.route("/sonic/on")
def Ultrasonic_on():
	print("FN Ultrasonic_on()")
	global WhileFlag
	WhileFlag = True
	try:
		while WhileFlag:
			GPIO.output(TRIG, True)
			time.sleep(0.00001)
			GPIO.output(TRIG, False)

			while GPIO.input(ECHO) == 0:
				#print('A')
				start = time.time()
			while GPIO.input(ECHO) == 1:
				#print('B')
				stop = time.time()

			check_time = stop - start
			distance = check_time/2 * 34300
			print("Distance : %.1f cm" % distance)
			time.sleep(0.4)
		return "ok"

	except Exception as identifier:
		print("except")
		WhileFlag = False
		return "fail"

@app.route("/sonic/off")
def Ultrasonic_off():
	global WhileFlag
	try:
		WhileFlag = False
		return "ok"
	except Exception as identifier:
		return "fail"

@app.route("/bz/on")
def Buzzer_on():
	try:
		GPIO.output(BUZZ, True)
		return "ok"
	except Exception as identifier:
		return "fail"

@app.route("/bz/off")
def Buzzer_off():
	try:
		GPIO.output(BUZZ, False)
		return "ok"
	except Exception as identifier:
		return "fail"

@app.route("/gpiocleanup")
def GPIO_CLEANUP():
	GPIO.cleanup()
	print("cleanup complete")
	return "ok"
	
if __name__ == "__main__":
	app.run(host = "0.0.0.0", port = "5555")



