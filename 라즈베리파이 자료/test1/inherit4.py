class Base:
	def __init__(self):
		self.b_who = "Base"
		print("It's Base constructor")
	def base_print(self):
		print("%s" % self.b_who)

class Derived(Base):
	def __init__(self):
		self.d_who = "Derived"
		print("It's Derived constructor")
		super().__init__()
	def derived_print(self):
		print("%s" % self.d_who)

b = Base()
d = Derived()
print("print(b.b_who): ", b.b_who)
print("print(d.d_who): ", d.d_who)
print("print(d.b_who): ", d.b_who)
print("d.base_print(): ", d.base_print())
