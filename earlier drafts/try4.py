make tree

before i even make tree, if i have a tree, how can i decide the right move?

each node has a unique id, children, value, and square

# 1 is win; -1 is lose

class Node(object):
	def __init__(self, square, player, children=[], value=0):
		self.children = children
		self.square = square
		self.value = value
		self.player = player

	def choose(self):
		for child in children:
			if child.value == (1 * player): # which becomes negative if computer
				return child

p = 1 # -1 is computer

a = Node(1, p, children=[b,c,d])
b = Node(2, p)
c = Node(3, p)
d = Node(4, p, value=1)

first, assume that O chooses 1
at the next level, X can choose 2, 3, or 4
check_win() on each of them. if it is true, we can stop there.
	value = more than 1, and O will choose that one