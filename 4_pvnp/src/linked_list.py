from ll_node import LLNode

class Linked_List(object):
	def __init__(self):
		self.h = None

	def __iter__(self):
		current = self.h
		while current:
			yield current
			current = current.next
	
	@property
	def head(self):
		return self.h
	
	@head.setter
	def head(self, val):
		self.h = val

	def isEmpty(self):
		return self.h is None

	def add_head(self, node):
		node.next = self.h
		self.h = node

	def print_list(self, list_head):
		if list_head:
			print(list_head.content)
			if list_head.next:
				self.print_list(list_head.next)

	def add_tail(self, list_head, val):
			if list_head is None:
				self.add_head(LLNode(val))
			else:
				while list_head.next:
					list_head = list_head.next
				list_head.next = LLNode(val)

	def remove(self, list_head, val):
		if list_head:
			a = list_head
			b = a.next
			while b and b.content != val:
				a = b
				b = b.next
			if b and b.content == val:
				a.next = b.next

	def has_cycle(self, list_head):
		if not list_head or not list_head.next:
			return False
		s = set()
		while list_head:
			if list_head in s:
				return True
				break
			s.add(list_head)
			list_head = list_head.next
		return False

	def merge(train1, train2):
		out = Linked_List()
		while train1 and train2:
			if train1.content > train2.content:
				out.add_tail(out.head, train1.content)
				train1 = train1.next
			else:
				out.add_tail(out.head, train2.content)
				train2 = train2.next
		while train1 or train2:
			if train1:
				out.add_tail(out.head, train1.content)
				train1 = train1.next
			else:
				out.add_tail(out.head, train2.content)
				train2 = train2.next
		return out.head
