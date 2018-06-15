class FirstClass(object):
	def __init__(self, name='world'):
		self.say_hello(name)

	def say_hello(self, name):
		print 'Method say_hello in FirstClass is called'
		print 'Hello ' + str(name)
