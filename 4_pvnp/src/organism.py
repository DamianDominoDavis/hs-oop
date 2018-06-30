class Organism(object):
	def __init__(self, hp=35, dmg=10):
		self.hp = hp
		self.dmg = 10

	def take_damage(self, damage):
		self.hp = self.hp - damage if self.hp >= damage else 0
