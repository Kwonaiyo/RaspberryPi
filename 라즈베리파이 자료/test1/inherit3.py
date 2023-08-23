class Base:
	b_who = "Base"
	def __init__(self):
		print("Base constructor")
	def base_print(self):
		print("%s" % self.b_who)

class Derived(Base):
	d_who = "Derived"
	def __init__(self):
		print("Derived constructor")
	def derived_print(self):
		print("%s" % self.d_who)

#b = Base()
d = Derived()
#b.base_print()
d.derived_print()

d.base_print()
print("print(d.b_who)")
print(d.b_who)
print("print(Base.b_who)")
print(Base.b_who)
