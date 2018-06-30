import sys
from game import Game

if __name__ == "__main__" and len(sys.argv) == 2:
	g = Game(sys.argv[1])
	g.place_wave()
	g.draw()
	g.get_input()
	while g.on:
		g.run_turn()
		g.draw()
		if g.on:
			g.get_input()
	print("Game Over")
