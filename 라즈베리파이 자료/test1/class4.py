class UnitClass:
	def __init__(self, species):
		self.species = species
	def show(self):
		print("species:%s " % self.species)

t = UnitClass("Terran")
t.show()
