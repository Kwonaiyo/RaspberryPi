from flask import Flask, request
import RPi.GPIO as GPIO

app = Flask(__name__)

LED_R = 22
LED_G = 24
LED_B = 26

GPIO.setmode(GPIO.BOARD)
GPIO.setup(LED_R, GPIO.OUT, initial = GPIO.LOW)
GPIO.setup(LED_G, GPIO.OUT, initial = GPIO.LOW)
GPIO.setup(LED_B, GPIO.OUT, initial = GPIO.LOW)

@app.route("/")
def helloworld():
	return "Hello World"

@app.route("/led")
def led():
	state = request.args.get("state", "error")
	if state == "R" or state == 'r':
		GPIO.output(LED_R, GPIO.HIGH)
		GPIO.output(LED_G, GPIO.LOW)
		GPIO.output(LED_B, GPIO.LOW)
		return "R ON"
	elif state == 'G' or state == 'g':
		GPIO.output(LED_R, GPIO.LOW)
		GPIO.output(LED_G, GPIO.HIGH)
		GPIO.output(LED_B, GPIO.LOW)
		return "G ON"
	elif state == 'B' or state == 'b':
		GPIO.output(LED_R, GPIO.LOW)
		GPIO.output(LED_G, GPIO.LOW)
		GPIO.output(LED_B, GPIO.HIGH)
		return "B ON"
	elif state == "error":
		return "쿼리스트링 state가 전달되지 않았습니다."
	else:
		return "잘못된 쿼리스트링이 전달되었습니다."
	return "ARE YOU OK?"

@app.route("/gpio/cleanup")
def gpioclean():
	GPIO.cleanup()
	return "GPIO cleanup"

if __name__=="__main__":
	app.run(host="0.0.0.0", port = "5555")
