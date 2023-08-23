class BaseClass:
	b_who = "BaseClass"
	def base_print(self):
		print("It's BaseClass, %s" % self.b_who)
	
class DerivedClass(BaseClass):
	d_who = "DerivedClass"
	def derived_print(self):
		print("It's DerivedClass, %s" % self.d_who)

b = BaseClass()
d = DerivedClass()
b.base_print()
d.derived_print()
