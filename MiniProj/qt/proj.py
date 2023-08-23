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
