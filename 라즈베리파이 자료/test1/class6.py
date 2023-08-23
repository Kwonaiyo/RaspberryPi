class UnitClass:
	def __init__(self, *args):
		self.species = args[0]
		self.hp = args[1]
		self.damage = args[1]
	def show(self):
		print("종족: %s, HP: %s, Damage : %s" % (self.species, self.hp, self.damage))

t = UnitClass("Terran", 50, 50)
t.show()
