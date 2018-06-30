from stack import Stack

def balanced(string):
	opening = '([{<'
	closing = ')]}>'
	conv = dict(zip(opening, closing))
	s = Stack()
	for ch in string:
		if ch in conv.keys():
			s.push(ch)
		elif ch in conv.values():
			o = s.pop()
			if conv[o] != ch:
				return False
	return s.isEmpty()

if __name__ == "__main__":
	print(balanced(input("string for ({[<>]}) balance? (use \"quotes\"): ")))
