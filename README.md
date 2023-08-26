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

+ 이미지<br>
  - 웹페이지<br>
![웹페이지](https://github.com/Kwonaiyo/RaspberryPi/blob/main/images/%EC%9B%B9%ED%8E%98%EC%9D%B4%EC%A7%80.PNG)
  - LED 동작버튼 클릭 시<br>
![LED동작시메시지](https://github.com/Kwonaiyo/RaspberryPi/blob/main/images/LED%20%EB%8F%99%EC%9E%91%EC%8B%9C%20%EB%A9%94%EC%8B%9C%EC%A7%80%20%ED%91%9C%EC%8B%9C.PNG)
  - LED가 켜진 모습<br>
![LED동작사진](https://github.com/Kwonaiyo/RaspberryPi/blob/main/images/LED%20%EB%8F%99%EC%9E%91%EC%82%AC%EC%A7%84.jpg)
  - Ultrasensor가 데이터 받아오는 모습<br>
![Ultra작동](https://github.com/Kwonaiyo/RaspberryPi/blob/main/images/Ultrasonic%20%EC%9E%91%EB%8F%99%EC%8B%9C%20%EC%B6%9C%EB%A0%A5%ED%99%94%EB%A9%B4.PNG)
  - QT 화면 구성<br>
![QT화면](https://github.com/Kwonaiyo/RaspberryPi/blob/main/images/qt%20%ED%99%94%EB%A9%B4.png)
  - 브래드보드 결선<br>
![브래드보드결선](https://github.com/Kwonaiyo/RaspberryPi/blob/main/images/%EB%9D%BC%EC%A6%88%EB%B2%A0%EB%A6%AC%20%ED%8C%8C%EC%9D%B4%20%EB%B0%8F%20%EB%B8%8C%EB%A0%88%EB%93%9C%EB%B3%B4%EB%93%9C%20%EA%B2%B0%EC%84%A0.jpg)

### 1. Webpage를 통한 센서 제어
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
### 2. Qt GUI를 통한 센서 제어
+ 파이썬 코드
```python
import sys
import RPi.GPIO as GPIO
import time
from PyQt5.QtWidgets import *
from PyQt5 import uic

form_class = uic.loadUiType("proj.ui")[0]

GPIO.setmode(GPIO.BCM)

#LED pins
LED_A = 10
LED_B = 9
LED_C = 11
GPIO.setup(LED_A, GPIO.OUT)
GPIO.setup(LED_B, GPIO.OUT)
GPIO.setup(LED_C, GPIO.OUT)

#Ultrasonic pins
TRIG = 23
ECHO = 20
GPIO.setup(TRIG, GPIO.OUT, initial=0)
GPIO.setup(ECHO, GPIO.IN)

#Buzzer pin
BUZZ = 17
GPIO.setup(BUZZ, GPIO.OUT, initial=0)

WhileFlag = False

class WindowClass(QMainWindow, form_class):
	def __init__(self):
		super().__init__()
		self.setupUi(self)

		self.btnLedOn.clicked.connect(self.fnLedOn)
		self.btnLedOff.clicked.connect(self.fnLedOff)
		self.btnGpioClear.clicked.connect(self.GPIOClear)
		self.btnSonicOn.clicked.connect(self.uSonicOn)
		self.btnSonicOff.clicked.connect(self.uSonicOff)
		self.btnBuzOn.clicked.connect(self.BuzzerOn)
		self.btnBuzOff.clicked.connect(self.BuzzerOff)

	def GPIOClear(self):
		GPIO.cleanup()
		print("GPIO clear!")
		
	def fnLedOn(self):
		GPIO.output(LED_A, 1)
		GPIO.output(LED_B, 1)
		GPIO.output(LED_C, 1)
		print("LED ON Clicked")

	def fnLedOff(self):
		GPIO.output(LED_A, 0)
		GPIO.output(LED_B, 0)
		GPIO.output(LED_C, 0)
		print("LED OFF Clicked")

	def uSonicOn(self):
		global WhileFlag
		WhileFlag = True
		try:
			while WhileFlag:
				GPIO.output(TRIG, True)
				time.sleep(0.00001)
				GPIO.output(TRIG, False)

				while GPIO.input(ECHO) == 0:
					start = time.time()
					#print("A")
				while GPIO.input(ECHO) == 1:
					stop = time.time()
					#print("B")
					
				check_time = stop - start
				distance = check_time/2 * 34300
				print("Distance : %.1f cm" % distance)
				time.sleep(0.4)
				QApplication.processEvents()
		except:
			print("error")
			sys.exit()
	#	pass

	def uSonicOff(self):
		global WhileFlag
		WhileFlag = False
		print("uSonicOff")

	def BuzzerOn(self):
		print("Buzzer ON")
		GPIO.output(BUZZ, 1)

	def BuzzerOff(self):
		print("Buzzer OFF")
		GPIO.output(BUZZ, 0)

if __name__ == "__main__":
	app = QApplication(sys.argv)
	myWindow = WindowClass()
	myWindow.show()
	app.exec_()
```

+ 프로젝트 진행하면서 힘들었던 점?
  - Ultrasensor가 거리 데이터를 받아오지 않아서 꽤나 고생했다.
    + 코드도 여러 번 확인해 봤으나 문제가 없었고, 라즈베리의 GPIO 핀을 바꿔봐도, 전선을 바꿔봐도, 작동 잘 되는 다른 센서로 바꿔봐도 해결되지 않았었다. => 알고보니 내가 바꿔본 전선들이 전부 불량이었다...
  - Ultrasensor가 받아온 데이터를 웹페이지로 보내주는 문제
    + 파이썬 파일에서 코드를 실행할 때는 print를 이용해서 출력해주면 됐었는데 Flask 서버에 데이터를 보내서 웹에서 보여주고 싶었으나 해결 방법을 찾지 못했다.
  - 파이썬에서 웹으로 데이터를 보내는 문제
    + 버튼 클릭 시 HTML에서 버튼이 클릭되었다는 정보를 Python에서 받아서 특정 함수를 실행한 이후 return을 통해 함수가 잘 실행되었는지(”ok”) 또는 예외가 발생하였는지(”fail”)를 return을 통해 다시 HTML로 정보를 넘겨주는데, Ultrasonic을 동작시키는 함수에서 while문을 통한 무한루프가 돌고있으므로 Ultrasonic OFF 버튼을 클릭하기 전까지는 ON 함수가 계속 동작되어 return값을 받아오지 않는다. return을 while문 내부에 선언해버리면 “ok” 데이터는 전달되지만 return을 만났을 때 함수가 종료되는 문제가 발생한다.  => 다른 방법을 통해 데이터를 HTML로 던져주고 싶었으나 아직 방법을 찾지 못함. 
   
+ 느낀점
많은 기능을 구현해보지는 못했지만, 간단하게나마 웹페이지 디자인도 해보고, 파이썬이라는 언어도 다뤄볼 수 있는 좋은 경험이었다.
