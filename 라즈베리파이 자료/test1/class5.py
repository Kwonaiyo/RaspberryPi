class UnitClass:
	def __init__(self, species, hp=50, mp=50):
		self.species = species
		self.hp = hp
		self.mp = mp
	def show(self):
		print("종족:%s, 체력:%s, 마나:%s" %(self.species, self.hp, self.mp))

t=UnitClass("Terran", 50, 50)
p=UnitClass("Protoss", 50, 50)
z=UnitClass("Zerg")
t.show()
p.show()
z.show()

