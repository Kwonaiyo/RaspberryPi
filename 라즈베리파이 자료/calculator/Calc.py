import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

#UI파일 연결
#단, UI파일은 Python 코드 파일과 같은 디렉토리에 위치해야한다.
form_class = uic.loadUiType("Calc.ui")[0]


inNums = ''
finalResult = ''

#화면을 띄우는데 사용되는 Class 선언
class WindowClass(QMainWindow, form_class):
	def __init__(self):
		super().__init__()
		self.setupUi(self)
		'''
		-------------------------------------
		이 부분에 시그널을 입력해야한다.
		시그널이 작동할 때 실행될 기능은 보통 이 클래스의 멤버함수로 작성한다.
		-------------------------------------
		'''
		#input = []

		#버튼에 기능을 연결하는 코드
		self.btnTest1.clicked.connect(self.btnTest1Function)
		self.btnTest2.clicked.connect(self.btnTest2Function)
		self.btnInputC.clicked.connect(self.InputClearFn)
		self.btnInputP.clicked.connect(self.InputPrintFn)
		self.btnTxtPrint.clicked.connect(self.PrintNum_1)
		self.btn0.clicked.connect(self.getNum0Fn)
		self.btn1.clicked.connect(self.getNum1Fn)
		self.btn2.clicked.connect(self.getNum2Fn)
		self.btn3.clicked.connect(self.getNum3Fn)
		self.btn4.clicked.connect(self.getNum4Fn)
		self.btn5.clicked.connect(self.getNum5Fn)
		self.btn6.clicked.connect(self.getNum6Fn)
		self.btn7.clicked.connect(self.getNum7Fn)
		self.btn8.clicked.connect(self.getNum8Fn)
		self.btn9.clicked.connect(self.getNum9Fn)
		self.btnPlus.clicked.connect(self.btnPlusClicked)
		self.btnMinus.clicked.connect(self.btnMinusClicked)
		self.btnMultiple.clicked.connect(self.btnMultipleClicked)
		self.btnDivide.clicked.connect(self.btnDivideClicked)
		self.btnResult.clicked.connect(self.btnResultClicked)

	input = []

	allValues = []
	def btnPlusClicked(self):
		global inNums
		global input
		tempCondition = ''
		if inNums == "":
			return
		else:
			print("inNums : %s" % inNums)
			if inNums != "":
				self.allValues.append(int(inNums))
			tempCondition = self.allValues[len(self.allValues)-1]
			print("tempCondition : %s" % tempCondition)
			if tempCondition == '+' or tempCondition == '-' or tempCondition == '*' or tempCondition == '/':
				return;
			else:
				self.allValues.append('+')
				tempCondition = self.allValues[len(self.allValues)-1]
				print("After if, tempC : %s" % tempCondition)
			print("allValues : %s" %self.allValues)
			inNums = ''

	def btnMinusClicked(self):
		global inNums
		if input[0] == "":
			return
		else:
			a = inNums
			inNums = ''
			allValues += '-'
	def btnMultipleClicked(self):
		if input[0] == "":
			return
		else:
			allValues += inNums
			inNums == ''
			allValues += '*'
	def btnDivideClicked(self):
		if input[0] == "":
			return
		else:
			allValues += inNums
			inNums == ''
			allValues += '/'
	def btnResultClicked(self):
		global inNums
		print("ResultbuttonClicked")
		if inNums != "":
			self.allValues.append(inNums)
			inNums = ""
		print("allValues %s" % self.allValues)
		print("len(allValues) %s" % len(self.allValues))
		global finalResult
		finalResult = ''
		if self.allValues ==  "":
			return
		else:
			while len(self.allValues) >= 3:
				print("IN WHILE :: len of allValues : %s" % len(self.allValues))
				print("IN WHILE :: allValues : %s" % self.allValues)
				A = int(self.allValues[0])
				B = self.allValues[1]
				C = int(self.allValues[2])
				if B == '+':
					result = A + C
					print("result : %s" %result)
					print("afterInsert : %s" %self.allValues)
					for i in range(0, 3, 1):
						self.allValues.pop(0)
					self.allValues.insert(0, result)
				if B == '-':
					pass
					'''
					result = A - C
					self.allValues.remove(A)
					self.allValues.remove(B)
					self.allValues.remove(C)
					self.allValues.insert(0, result)
					'''
				if B == '*':
					result = A * C
					pass
					'''
					self.allValues.remove(A)
					self.allValues.remove(B)
					self.allValues.remove(C)
					self.allValues.insert(0, result)
					'''
				if B == '/':
					result = A / C
					self.allValues.remove(A)
					self.allValues.remove(B)
					self.allValues.remove(C)
					self.allValues.insert(0, result)
			#while 빠져나옴 .. 
			
			finalResult = result
			print("fianlResult : %s" % finalResult)
			self.allValues.remove(finalResult)
			print("Test1 : %s" % self.allValues)
		result = ''
		self.txt_2.setPlainText("result: " + str(finalResult))
		#		print("A: %s" % a)
		#	for vlaues in self.allValues[len(self.allValues) %

	#btnTest1이 눌리면 작동할 함수::
	def btnTest1Function(self):
		print("btnTest1 Clicked")
		self.btnResultClicked()
	#btnTest2가 눌리면 작동할 함수::
	def btnTest2Function(self):
		print("btnTest2 Clicked")
		print(input)
	def InputClearFn(self):
		self.input.clear()
		self.txt_1.clear()
		global inNums
		self.allValues.clear()
		inNums = ''
		print("Input Clear Completed :)")

	#Print Method
	def InputPrintFn(self):	#InputPrint
		print("self.input: %s" % self.input)
		print("inNums: %s" % inNums)
		print("self.allValues: %s" % self.allValues)
	def PrintNum_1(self):	#btnTxtPrint
		self.txt_1.clear()
		self.txt_1.setPlainText(inNums)

	def getNum(self, x):
		global inNums
		self.input.append(x)
		a = str(x)
		inNums += a

	def getNum0Fn(self):
		self.getNum(0)
		'''
		global inNums
		self.input.append(0)
		inNums += '0'
		'''
	def getNum1Fn(self):
		global inNums
		self.input.append(1)
		inNums += '1'
	def getNum2Fn(self):
		global inNums
		self.input.append(2)
		inNums += '2'
	def getNum3Fn(self):
		global inNums
		self.input.append(3)
		inNums += '3'
	def getNum4Fn(self):
		global inNums
		self.input.append(4)
		inNums += '4'
	def getNum5Fn(self):
		global inNums
		self.input.append(5)
		inNums += '5'
	def getNum6Fn(self):
		global inNums
		self.input.append(6)
		inNums += '6'
	def getNum7Fn(self):
		global inNums
		self.input.append(7)
		inNums += '7'
	def getNum8Fn(self):
		global inNums
		self.input.append(8)
		inNums += '8'
	def getNum9Fn(self):
		global inNums
		self.input.append(9)
		inNums += '9'
	


if __name__ == "__main__":
	#QApplication : 프로그램을 실행시켜주는 클래스
	app = QApplication(sys.argv)

	#WindowClass의 인스턴스 생성
	myWindow = WindowClass()

	#프로그램 화면을 보여주는 코드
	myWindow.show()

	#프로그램을 이벤트루프로 진입시키는(프로그램을 작동시키는) 코드
	app.exec_()
