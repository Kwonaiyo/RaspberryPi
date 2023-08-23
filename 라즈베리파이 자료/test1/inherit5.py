class BaseClass:
	def show(self):
		print("I'm BaseClass")
class DerivedClass(BaseClass):
	def show(self):
		print("I'm DerivedClass")
		super().show()

b = BaseClass()
d = DerivedClass()

b.show()
d.show()
