from flask import Flask, request

import RPi.GPIO as GPIO

app = Flask(__name__)

LED = 8
GPIO.setup(GPIO.BOARD)
GPIO.setup(LED, GPIO.OUT, initial=GPIO.LOW)

@app.route("/led/<state>")
def led(state):
	if(state == "ON"):
		GPIO.output(LED, GPIO.HIGH)
		return "LED ON"
	elif(state == "off"):
		GPIO.output(LED, GPIO.LOW)
		return "LED OFF"
	else:
		return "ERROR"

if __name__ == "__main__":
	app.run(host="0.0.0.0")
