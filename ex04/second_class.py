from first_class import FirstClass
from random import *

class SecondClass(FirstClass):
	def __init__(self, name='cbrill'):
		name = name + ', your number is ' + str(self.roll_dice())
		super().__init__(name)
	def roll_dice(self):
		print('Method roll_dice is called from SecondClass')
		return randint(1,6)
