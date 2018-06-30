from node import Node

class Queue(object):
	def __init__(self):
		self.front = self.rear = None

	@property
	def front(self):
		return self._front
	
	@front.setter
	def front(self, value):
		self._front = value
	
	@property
	def rear(self):
		return self._rear
	
	@rear.setter
	def rear(self, value):
		self._rear = value

	def __iter__(self):
		now = self.front
		while now:
			yield now
			now = now.next
	
	def isEmpty(self):
		return self.front == self.rear == None

	def enqueue(self, data):
		if self.isEmpty():
			self.front = self.rear = Node(data)
		else:
			self.rear.next = Node(data)
			self.rear = self.rear.next

	def dequeue(self):
		if self.isEmpty():
			return None
		out = self.front
		self.front = self.front.next
		if not self.front:
			self.rear = None
		return out.data

	def size(self):
		if self.isEmpty():
			return 0
		l = 0
		c = self.front
		while c:
			l += 1
			c = c.next
		return c

	def __str__(self):
		return '[' + ', '.join(str(node.data) for node in self) + ']'
