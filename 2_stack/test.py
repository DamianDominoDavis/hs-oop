from stack import Stack

s = Stack()
[s.push(x) for x in range(10)]
print(s)
c = s.pop()
while c:
	print(c)
	c = s.pop()
	print(s)
