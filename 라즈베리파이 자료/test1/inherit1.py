class BaseClass:
	def base_print(self):
		''' Super Class '''
		print("BaseClass")
class DerivedClass(BaseClass):
	''' Sub Class '''
	def derived_print(self):
		print("DerivedClass")
b = BaseClass()			#부모객체생성
d = DerivedClass()  #자식객체생성
b.base_print()			#부모객체의 base_print() 호출
d.derived_print()		#자식객체의 derived_print() 호출
d.base_print()			#자식객체에서 부모객체의 메소드 호출 가능
