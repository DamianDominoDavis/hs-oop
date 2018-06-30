from stack import Stack

def itoabase(inp, b):
	conv = dict(zip([i for i in range(16)], [str(x) for x in range(10)] + [chr(c) for c in range(ord('A'), ord('F')+1)]))
	s = Stack()
	try:
		assert 2 <= b <= 16
		while inp > 0:
			s.push(conv[inp%b])
			inp //= b
		return ''.join(x for x in s)
	except:
		return None

if __name__ == '__main__':
	inp = int(input("int base 10? "))
	b = int(input("convert to base 2-16? "))
	print(itoabase(inp, b))
