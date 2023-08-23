# 라즈베리 파이 공부
+ 처음으로 파이썬 언어 사용해봄
+ Flask로 웹 페이지도 처음 만들어봄
+ 라즈베리파이에 LED센서, Ultrasonic센서, Buzzer, 작은 디스플레이, 세그먼트 등 연결해서 동작시켜봄
## 미니프로젝트_라즈베리파이를 통한 센서 제어
  개발인원 : 1명  
  개발기간 : 2023.06.16 ~ 2023.06.18  
  주요기능 : LED 제어, Ultrasensor 제어, Buzzer 제어  
  개발언어 : Python, CSS, HTML, Javascript
  + Webpage를 통한 센서 제어
  + PyQt를 이용한 센서 제어
## 1. Webpage를 통한 센서 제어
+ 웹페이지 구성 코드
```html
  <!DOCKTYPE html>
<html>
  <head>
  	<meta charset="UTF-8">
  	<title>Project HTML</title>
  	<link rel="stylesheet" href="{{url_for('static', filename='style.css')}}">
  </head>
  <body>
  	<div class="container">
  		<div class="header">
  			<h2>Controll Webpage</h2>
  		</div>
  		<div class="main">
  			<div>
  				<button style="background-color: rgb(200,200,200);" onclick="led_on()">LED ON</button>
  				<button style="background-color: rgb(200,200,200);" onclick="led_off()">LED OFF</button>
  			</div>
  		</div>
  		<div class="main">
  			<div>
  				<button style="background-color: rgb(123, 123, 188);" onclick="Ultrasonic_on()">Ultrasonic ON</button>
  				<button style="background-color: rgb(123, 123, 188);" onclick="Ultrasonic_off()">Ultrasonic OFF</button>
  			</div>
  		</div>
  		<div class="main">
  			<div>
  				<button style="background-color: rgb(222, 222, 222);" onclick="Buzzer_on()">Buzzer ON</button>
  				<button style="background-color: rgb(222, 222, 222);" onclick="Buzzer_off()">Buzzer OFF</button>
  			</div>
  		</div>
  		<div class="main">
  			<div>
  				<button style="background-color: rgb(90, 80, 70);" onclick="GPIO_CLEANUP()">GPIO_CLEANUP</button>
  			</div>
  		</div>
  		</div>
  		<div id="result">
  
  		</div>
  	</div>
  	<script>
  		function led_on(){
  			fetch("/led/on")
  				.then(response=> response.text())
  				.then(data=> {
  					console.log(data);
  					let result = document.querySelector("#result");
  					if(data=="ok"){
  						result.innerHTML = "<h1 style='text-align: center;'>LED is running</h1>";
  					}else{
  						result.innerHTML = "<h1 style='text-align: center;'>led_on error</h1>";
  					}
  				});
  		}
  		function led_off(){
  			fetch("/led/off")
  				.then(response=> response.text())
  				.then(data=> {
  					console.log(data);
  					let result = document.querySelector("#result");
  					if(data=="ok"){
  						result.innerHTML = "<h1 style='text-align: center;'>LED is stopping</h1>";
  					}else{
  						result.innerHTML = "<h1 style='text-align: center;'>led_off error</h1>";
  					}
  				});
  		}
  		function Ultrasonic_on(){
  			fetch("/sonic/on")
  				.then(response=> response.text())
  				.then(data=> {
  					console.log(data);
  					let result = document.querySelector("#result");
  					if(data=="ok"){
  						result.innerHTML = "<h1 style='text-align: center;'>Ultrasonic is running</h1>";
  					}else{
  						result.innerHTML = "<h1 style='text-align: center;'>sonic_on err</h1>";
  					}
  				});
  		}
  		function Ultrasonic_off(){
  			fetch("/sonic/off")
  				.then(response=> response.text())
  				.then(data=> {
  					console.log(data);
  					let result = document.querySelector("#result");
  					if(data=="ok"){
  						result.innerHTML = "<h1 style='text-align: center;'>Ultrasonic is stopped</h1>";
  					}else{
  						result.innerHTML = "<h1 style='text-align: center;'>sonic_off error</h1>";
  					}
  				});
  		}
  		function Buzzer_on(){
  			fetch("/bz/on")
  				.then(response=> response.text())
  				.then(data=> {
  					console.log(data);
  					let result = document.querySelector("#result");
  					if(data=="ok"){
  						result.innerHTML = "<h1 style='text-align: center;'>Buzzer is singing</h1>";
  					}else{
  						result.innerHTML = "<h1 style='text-align: center;'>bz_on error</h1>";
  					}
  				});
  		}			
  		function Buzzer_off() {
  			fetch("/bz/off")
  				.then(response=> response.text())
  				.then(data=> {
  					console.log(data);
  					let result = document.querySelector("#result");
  					if(data=="ok"){
  						result.innerHTML = "<h1 style='text-align: center;'>Buzzer is stopped</h1>";
  					}else{
  						result.innerHTML = "<h1 style='text-align: center;'>bz_off error</h1>";
  					}
  				});
  		}
  		function GPIO_CLEANUP(){
  			fetch("gpiocleanup")
  				.then(response=> response.text())
  				.then(data=> {
  					console.log(data);
  					let result = document.querySelector("#result");
  					if(data=="ok"){
  						result.innerHTML = "<h1 style='text-align: center;'>GPIO cleanup complete</h1>";
  					}else{
  						result.innerHTML = "<h1 style='text-align: center;'>something is wrong. cleanup fail</h1>";
  					}
  				});
  		}
  	</script>
  </body>
</html>
```
+ 파이썬 코드
```
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
```
