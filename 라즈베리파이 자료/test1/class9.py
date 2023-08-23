class Unit:
	def __init__(self, species, hp, damage):
		self.__species = species
		self.hp = hp
		self.damage = damage
	def show(self):
		print(self.__species, self.hp, self.damage)
	def __show_status(self):
		print("전투준비완료")

t = Unit("Terran", 555, 5)
t.show()
#t.show_status()  #show_status는 private이기 때문에 외부에서 호출할 수 없다.

