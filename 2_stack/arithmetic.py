from stack import Stack
from functools import reduce
import operator

s = Stack()
i = input("Enter values (\"1 5 ...\"): ")
[s.push(int(n)) for n in i.split()]
print(s)
print("Count:", s.size())
print("Sum:", sum(s))
print("Product:", reduce(operator.mul, s))
print("Mean:", sum(s) / s.size())
print("Min:", reduce(min, s))
print("Max:", reduce(max, s))
