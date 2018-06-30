import sys
from stack import Stack

def balanced(string):
	opening = '([{<'
	closing = ')]}>'
	conv = dict(zip(opening, closing))
	s = Stack()
	for ch in string:
		if ch in conv.keys():
			s.push(ch)
		elif ch in conv.values() and conv[s.pop()] != ch:
			return False
	return True

if __name__ == "__main__":
	usg = "usage: python3 parentheses.py \"string\""
	print(usg if len(sys.argv) != 2 else balanced(sys.argv[1]))
