class UnitClass:
	def __init__(self, hp, damage):
		self.hp = hp
		self.damage = damage
	def show(self):
		print(self.hp, self.damage)

t = UnitClass(59, 666)
t.show()

t.species = "Terran"
print(t.species)
t.show()
