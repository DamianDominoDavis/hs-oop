class FirstClass():
	def __init__(self, n='world'):
		self.say_hello()
		print('Hello ' + n)
	def say_hello(self):
		print('Method say_hello in FirstClass is called')
