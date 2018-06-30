from stack import Stack

def strrev(str):
	s = Stack()
	[s.push(x) for x in str]
	return ''.join([x for x in s])

if __name__ == '__main__':
	inp = input("String to reverse? ")
	print(strrev(inp))
