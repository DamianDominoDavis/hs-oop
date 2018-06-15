from first_class import FirstClass
from random import *

class SecondClass(FirstClass):
	def __init__(self, name='cbrill'):
		super(SecondClass, self).__init__()
		message = 'Hello cbrill, your number is ' + self.roll_dice()
		self.hello(message)

	def roll_dice(self):
		print 'Method roll_dice is called from SecondClass'
		return str(randint(1,6))
