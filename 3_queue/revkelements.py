from queue import Queue
from stack import Stack

def revkelements(string, k):
	s = Stack()
	qa = Queue()
	qb = Queue()
	[qa.enqueue(x) for x in string]
	[s.push(qa.dequeue()) for x in range(k)]
	[qb.enqueue(s.pop()) for x in s]
	qb.rear.next = qa.front
	return ''.join([str(x.data) for x in qb])

if __name__ == '__main__':
	inp = input("String? ")
	k = input("reverse first K e? ")
	print(revkelements(inp, int(k)))
