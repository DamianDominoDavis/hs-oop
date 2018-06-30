from singly_list import SinglyList
from random import randint

def train(size, parity):
	out = SinglyList()
	if parity == 0:
		size = 2 * int(size/2)
	elif size % 2 == 0:
		size -= 1
	for x in range(size, 0, -2):
		out.add_tail(out.head, x)
	return out

list_a = SinglyList()
[list_a.add_tail(list_a.head, x) for x in range(8, 3, -1)]
list_a.remove(list_a.head, 6)
list_a.print_list(list_a.head)
print('Cycle? ', end='')
print('yes' if list_a.has_cycle(list_a.head) else 'no')
tail = list_a.head
while tail.next:
	tail = tail.next
tail.next = list_a.head
print('Cycle? ', end='')
print('yes' if list_a.has_cycle(list_a.head) else 'no')
tail.next = None
list_a = train(10, 0)
list_b = train(10, 1)
print('Merge:')
train = SinglyList.merge(list_a.head, list_b.head)
list_a.print_list(train)
list_c = SinglyList()
[list_c.add_tail(list_c.head, randint(1,20)) for x in range(randint(7,13))]
list_c.sort()
print("Random sorted list:")
list_c.print_list(list_c.h)
