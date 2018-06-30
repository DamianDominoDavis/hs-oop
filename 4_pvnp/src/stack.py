from qs_node import QSNode

class Stack(object):
	def __init__(self):
		self.e = []

	@property
	def e(self):
		return self._e

	@e.setter
	def e(self, value):
		self._e = value

	def __iter__(self):
		for x in self.e[::-1]:
			yield x
	
	def isEmpty(self):
		return not self.e

	def push(self, data):
		node = QSNode(data)
		if not self.isEmpty():
			node.next = self.e[-1]
		self.e.append(node)

	def pop(self):
		return None if self.isEmpty() else self.e.pop()

	def peek(self):
		return self.e[-1].data if self.e else None

	def size(self):
		return len(self.e)

	def __str__(self):
		return '[' + ', '.join(str(node.data) for node in self.e) + ']'
