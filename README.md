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
```python
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
+ 프로젝트 진행하면서 힘들었던 점?
  - Ultrasensor가 거리 데이터를 받아오지 않아서 꽤나 고생했다..
    + 코드도 여러 번 확인해 봤으나 문제가 없었고, 라즈베리의 GPIO 핀을 바꿔봐도, 전선을 바꿔봐도, 작동 잘 되는 다른 센서로 바꿔봐도 해결되지 않았었다. => 알고보니 내가 바꿔본 전선들이 전부 불량이었다...
  - Ultrasensor가 받아온 데이터를 웹페이지로 보내주는 문제
    + 파이썬 파일에서 코드를 실행할 때는 print를 이용해서 출력해주면 됐었는데 Flask 서버에 데이터를 보내서 웹에서 보여주고 싶었으나 해결 방법을 찾지 못했다.
  - 파이썬에서 웹으로 데이터를 보내는 문제
    + 버튼 클릭 시 HTML에서 버튼이 클릭되었다는 정보를 Python에서 받아서 특정 함수를 실행한 이후 return을 통해 함수가 잘 실행되었는지(”ok”) 또는 예외가 발생하였는지(”fail”)를 return을 통해 다시 HTML로 정보를 넘겨주는데, Ultrasonic을 동작시키는 함수에서 while문을 통한 무한루프가 돌고있으므로 Ultrasonic OFF 버튼을 클릭하기 전까지는 ON 함수가 계속 동작되어 return값을 받아오지 않는다. return을 while문 내부에 선언해버리면 “ok” 데이터는 전달되지만 return을 만났을 때 함수가 종료되는 문제가 발생한다.  => 다른 방법을 통해 데이터를 HTML로 던져주고 싶었으나 아직 방법을 찾지 못함. 
   
+ 느낀점
많은 기능을 구현해보지는 못했지만, 간단하게나마 웹페이지 디자인도 해보고, 파이썬이라는 언어도 다뤄볼 수 있는 좋은 경험이었다.
