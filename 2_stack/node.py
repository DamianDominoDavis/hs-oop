class Node(object):
	def __init__(self, value):
		self.data = value
		self.next = None

	@property
	def data(self):
		return self._data
	
	@data.setter
	def data(self, val):
		self._data = val

	@property
	def next(self):
		return self._next
	
	@next.setter
	def next(self, val):
		self._next = val
