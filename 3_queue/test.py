from queue import Queue

q = Queue()
[q.enqueue(x) for x in range(10)]
print(q)
c = q.dequeue()
while c:
	print(c.data)
	print(q)
	c = q.dequeue()
