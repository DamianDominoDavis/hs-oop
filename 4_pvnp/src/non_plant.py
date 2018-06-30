from organism import Organism

class Non_Plant(Organism):
	worth = 20

	def __init__(self):
		super(Organism, self).__init__()
		self.hp = 80
		self.dmg = 5

	def attack(self, plant):
		plant.take_damage(self.dmg)
