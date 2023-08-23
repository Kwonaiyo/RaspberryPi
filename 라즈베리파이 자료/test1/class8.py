class UnitClass:
	def __init__(self, species, hp=1111, damage=50):
		self.__species = species # __ 언더바 두개 붙이면 private  속성을 가진다.
		self.hp = hp
		self.damage = damage
	def show(self):
		print(self.__species, self.hp, self.damage)

t = UnitClass("Terran")
t.show()

print(t.hp)
print(t.damage)
#print(t.__species)   #class 외부에서 private 속성에 접근할 수 없다. 
