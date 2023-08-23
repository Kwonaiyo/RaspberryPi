from flask import Flask
import RPi.GPIO as GPIO

app = Flask(__name__)

LED_R = 22
LED_G = 24
LED_B = 26

GPIO.setmode(GPIO.BOARD)	#BOARD : 커넥터 pin번호 사용
GPIO.setup(LED_R, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(LED_G, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(LED_B, GPIO.OUT, initial=GPIO.LOW)

@app.route("/")
def helloworld():
	return "HELLO WORLD"

@app.route("/led/<color>")
def led(color):
	if color == "R" or color == "r":
		GPIO.output(LED_R, GPIO.HIGH)
		GPIO.output(LED_G, GPIO.LOW)
		GPIO.output(LED_B, GPIO.LOW)
		return "Red ON"
	elif color == "G" or color == "g":
		GPIO.output(LED_R, GPIO.LOW)
		GPIO.output(LED_G, GPIO.HIGH)
		GPIO.output(LED_B, GPIO.LOW)
		return "Green ON"
	elif color == "B" or color == "b":
		print("B")
		GPIO.output(LED_R, GPIO.LOW)
		GPIO.output(LED_G, GPIO.LOW)
		GPIO.output(LED_B, GPIO.HIGH)
		return "Blue ON"
	else:
		GPIO.setup(LED_R, GPIO.LOW)
		GPIO.setup(LED_G, GPIO.LOW)
		GPIO.setup(LED_B, GPIO.LOW)
		return "Wrong value, All OFF"

@app.route("/gpio/cleanup")
def gpioCleanup():
	GPIO.cleanup()
	return "cleanup Complete"

if __name__=="__main__":
	app.run(host="0.0.0.0", port = "5555")
