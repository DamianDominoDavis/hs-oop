import random
from plant import Plant
from non_plant import Non_Plant
from linked_list import Linked_List
from queue import Queue
from stack import Stack
from wave import Wave
from card import Card
from colors import Colors

class Game(object):
	def __init__(self, file):
		with open(file, 'r') as f:
			self.cash, self.height, self.width = [int(x) for x in f.readline().split(' ')]
			self.waves = []
			self.waves_num = 0
			for line in iter(f.readline, ''):
				self.waves.append(Wave(*[int(x) for x in line.split(' ')]))
				self.waves_num += 1
			self.waves.sort(key=lambda x: x.wave_num)
		self.board = []
		for y in range(self.height):
			row = []
			for x in range(self.width):
				row.append(Queue())
			self.board.append(row)
		self.on = True
		self.turn = 0
		self.nonplants = 0
		self.deck = Stack()
		for x in range(100):
			card = Card(random.randint(1,5))
			self.deck.push(card)

	def draw(self):
		#print("$", self.cash, "\nWaves: ", self.waves_num, ", Turn ", self.turn ,sep='')
		print("$", self.cash, " ", self.turn//60, ":", "{:02}".format(self.turn%60), "\n", self.waves_num, " waves and ", self.nonplants, " enemies remain", sep='')
		s = ' '.join([str(i) for i in range(self.width - 1)])
		print(' ', s)
		for row in range(self.height):
			s = []
			for col in range(self.width):
				if self.is_plant(row, col):
					char = 'P'
				elif self.is_nonplant(row, col):
					size = self.board[row][col].size()
					char = str(size) if size < 10 else '#'
				else:
					char = '.'
				s.append(char)
			print(row, ' ', ' '.join(s), sep='')

	def is_nonplant(self, row, col):
		return False if row >= self.height or col >= self.width else isinstance(self.board[row][col].peek(), Non_Plant)

	def is_plant(self, row, col):
		return isinstance(self.board[row][col].peek(), Plant)

	def remove(self, row, col):
		guy = self.board[row][col].dequeue()
		if isinstance(guy, Non_Plant):
			self.cash += Non_Plant.worth
			self.nonplants -= 1
	
	def place_nonplant(self, row):
		self.board[row][-1].enqueue(Non_Plant())
		self.nonplants += 1

	def place_plant(self, row, col):
		if row >= self.height or col >= self.width or row < 0 or col < 0:
			raise ValueError(str(row) + " " + str(col) + " aint no coordinates I ever heard of! do they speak english in " + str(row) + " " + str(col) + "?!")
		elif self.board[row][col] is self.board[row][-1]:
			raise ValueError("you're out on the edge, yeah! and the HOA says no planting on the edge.")
		elif self.is_plant(row, col) or self.is_nonplant(row, col):
			raise ValueError("easy there xhibit, you've already got something in that spot.")
		if self.cash <= Plant.cost:
			raise ValueError("poor boy from a poor family, spare not their lives so you can afford me.")
		self.cash -= Plant.cost
		self.board[row][col].enqueue(Plant())
		
	def place_wave(self):
		if len(self.waves) > 0 and self.waves[0].wave_num == self.turn:
			w = self.waves.pop(0)
			while w.num:
				self.place_nonplant(w.row)
				w.num -= 1
			self.waves_num -= 1

	def plant_turn(self):
		for row in range(self.height):
			for col in range(self.width - 1):
				if self.is_plant(row, col):
					p = self.board[row][col].peek()
					col += 1
					while col <= self.width and not self.is_nonplant(row, col):
						col += 1
					if self.is_nonplant(row, col):
						n = self.board[row][col].peek()
						p.attack(n)
						if n.hp == 0:
							self.remove(row, col)

	def nonplant_turn(self):
		for row in range(self.height):
			for col in range(self.width):
				if self.is_nonplant(row, col):
					nq = self.board[row][col]
					if col == 0:
						self.on = False
					elif self.is_plant(row, col - 1):
						p = self.board[row][col - 1].peek()
						for n in nq:
							n.data.attack(p)
						if p.hp == 0:
							self.remove(row, col - 1)
							p = None
					if not self.is_plant(row, col - 1):
						self.board[row][col - 1] = self.board[row][col]
						self.board[row][col] = Queue()
		return True

	def run_turn(self):
		self.turn += 1
		for row in range(self.height):
			for col in range(self.width - 1):
				if self.is_plant(row,col):
					self.board[row][col].peek().weaken_powerup()
		self.plant_turn()
		self.nonplant_turn()
		if not self.on or self.waves_num == self.nonplants == 0:
			self.on = False
		else:
			self.place_wave()

	def draw_card(self):
		if self.cash >= Card.cost:
			self.cash -= Card.cost
			return self.deck.pop()
		else:
			print("flash the plastic all you like, but you can't actually afford that.")

	def get_input(self):
		while True:
			ui = input("Action?\n  [ROW COL] to place plant ($" + str(Plant.cost) + ")\n  [C] to draw a powerup card ($" + str(Card.cost) + ")\n  [Q] to quit\n  [ENTER] to do nothing?\n")
			if (len(ui) > 0):
				if (len(ui) == 1):
					if (ui.lower() == 'c'):
						self.draw_card()
						break
					elif (ui.lower() == 'q'):
						self.over = True
						break
					else:
						print("I... what? \"" + ui + "\"?")
				else:
					try:
						row, col = [int(x) for x in ui.split()]
						self.place_plant(row, col)
						break
					except ValueError as e:
						print(e)
						#print("Invalid input \"" + ui + "\"")
			else:
				break
