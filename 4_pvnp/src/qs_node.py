class QSNode(object):
	def __init__(self, value, next=None):
		self.data = value
		self.next = next

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
