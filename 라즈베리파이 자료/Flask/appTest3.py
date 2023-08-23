from flask import Flask
import RPi.GPIO as GPIO

app = Flask(__name__)

LED_R = 25		#GPIO25, PIN-22
LED_G = 8			#GPIO8,  PIN-24
LED_B = 7			#GPIO7,  PIN-26

GPIO.setmode(GPIO.BCM)	#GPIO번호 사용
GPIO.setup(LED_R, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(LED_G, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(LED_B, GPIO.OUT, initial=GPIO.LOW)
 
@app.route("/")
def helloworld():
	return "Hello World"

@app.route("/led/R")
def ledR():
	GPIO.output(LED_R, GPIO.HIGH)
	GPIO.output(LED_G, GPIO.LOW)
	GPIO.output(LED_B, GPIO.LOW)
	return "LED_R ON"

@app.route("/led/G")
def ledG():
	GPIO.output(LED_R, GPIO.LOW)
	GPIO.output(LED_G, GPIO.HIGH)
	GPIO.output(LED_B, GPIO.LOW)
	return "LED_G ON"

@app.route("/led/B")
def ledB():
	GPIO.output(LED_R, GPIO.LOW)
	GPIO.output(LED_G, GPIO.LOW)
	GPIO.output(LED_B, GPIO.HIGH)
	return "LED_B ON"

@app.route("/all_on")
def ledAllOn():
	GPIO.output(LED_R, GPIO.HIGH)
	GPIO.output(LED_G, GPIO.HIGH)
	GPIO.output(LED_B, GPIO.HIGH)
	return "ALL LED ON"

@app.route("/led/off")
def ledOff():
	GPIO.output(LED_R, GPIO.LOW)
	GPIO.output(LED_G, GPIO.LOW)
	GPIO.output(LED_B, GPIO.LOW)
	return "ALL LED OFF"

@app.route("/gpio/cleanup")
def cleanup():
	GPIO.cleanup()
	return "cleanup Complete"

if __name__ == "__main__":
	app.run(host="0.0.0.0", port="5555")
