from random import randint, getrandbits
from singly_list import SinglyList

def yard(alice, bob):
	cars = sorted([car for car in alice] + [car for car in bob])
	return cars

if __name__ == '__main__':
	alice = []
	bob = []
	for x in range(randint(10, 15)):
		who = alice if getrandbits(1) else bob
		who.append(randint(1,20))
	print("Alice:", alice, sep=' ')
	print("Bob:", bob, sep=' ')
	carol = SinglyList()
	dave = SinglyList()
	[carol.add_tail(carol.h, x) for x in alice + bob]
	carol.sort()
	while carol.size() > 2:
		dave.add_tail(dave.h, carol.h)
		carol.remove(carol.h, carol.h)
	print("Carol:", carol, sep=' ')
	print("Dave:", dave, sep=' ')
	