# tic tac toe

import random

def flatten(x):
	"""Flattens any list of lists to the nth power recursively!"""
	new_list = []

	def another_flatten(y): # to keep scope
		for element in y:
			if type(element) == list:
				another_flatten(element)
			else:
				new_list.append(element)

		return new_list

	return another_flatten(x)

class Board(object):
	def __init__(self):
		length = 3
		width = 3

		self.board = []

		for row in range(length):
			self.board.append(['-'] * width)

	def print_board(self):
		for row in self.board:
			print ' '.join(row)

	def print_win(self, marker):
		if marker == 'x':
			player = 'You'
		elif marker == 'o':
			player = 'The computer'
		print 'Game over! {} won!'.format(player)

	def check_win(self, marker):
		xs = [0,1,0,-1,-1,-1,1,1]
		ys = [1,0,-1,0,-1,1,1,-1]

		def check_for_x(row, col):
			if row in range(len(self.board)):
				if col in range(len(self.board[0])):
					if self.board[row][col] == marker:
						return True

		for row in range(len(self.board)):
			for col in range(len(self.board[0])):
				#print row, col
				history = []

				if check_for_x(row, col): # depth 1
					history.append([row,col])

					for i in range(len(xs)): # I can do this recursively
						new_row = row + xs[i]
						new_col = col + ys[i]

						if check_for_x(new_row, new_col): # depth 2
							history.append([new_row, new_col])

							new_row += xs[i]
							new_col += ys[i]

							if check_for_x(new_row, new_col): # depth 3
								history.append([new_row, new_col])
								if len(history) == 3: # recursively, this should check after every append
									self.print_win(marker)
									return True
							else:
								history.pop()
					else:
						#print 'hx to this point is', history
						history.pop()

				#print history

	def check_full(self):
		for row in self.board:
			for entry in row:
				if entry == '-':
					return False
		print 'The board is full. Game over.'
		return True

	def status(self):
		if self.check_win('x'):
			return 1
		elif self.check_win('o'):
			return -1		
		elif self.check_full():
			return 0
		else:
			return None


class Player(object):
	def __init__(self, board, person=True):
		self.person = person
		self.board = board

		if person == True:
			self.marker = 'x'
		else:
			self.marker = 'o'

	def move(self):
		if self.person:
			row, col = self.ask_move()
		else: # AI for now
			row, col = self.computer_move()
		
		if self.board.board[row][col] == '-':
			self.board.board[row][col] = self.marker
		else:
			if self.person:
				print 'That space is already taken. Try another.'
			self.move()

	def computer_move(self):
		row = random.randint(0, len(self.board.board) - 1)
		col = random.randint(0, len(self.board.board[0]) - 1)
		#print 'Computer move is {}, {}'.format(row, col)
		return row, col

	def ask_move(self):
		row = raw_input('What row? ')
		while row == '':
			row = raw_input('What row? ')

		row = int(row) - 1

		while (row >= len(self.board.board) or row < 0 or row == ''):
			print "That's outside of the board. Try another."
			row = int(raw_input('What row? ')) - 1
		
		col = raw_input('What column? ' )
		while col == '':
			col = raw_input('What column? ' )

		col = int(col) - 1

		while (col >= len(self.board.board[0]) or col < 0 or col == ''):
			print "That's outside of the board. Try another."
			col = int(raw_input('What column? ' )) - 1

		return row, col

class MiniMaxPlayer(Player):
	pass

class Game(object):
	def __init__(self):
		board = Board()
		turns = 0
		while turns <= 5:
			turns += 1
			print 'turn {}'.format(turns)
			person = Player(board)
			computer = Player(board, person=False)

			person.move() # do sth to have either comp or person go first
			
			if board.check_full():
				if not (board.check_win('x') or board.check_win('o')):
					print 'No one wins.'
				break

			computer.move()

			if board.check_full():
				if not (board.check_win('x') or board.check_win('o')):
					print 'No one wins.'
				break

			board.print_board()

			if board.check_win('x') or board.check_win('o'):
				break

def board_test():
	board = Board()
	board.board[2][0], board.board[2][1], board.board[2][2] = ['x'] * 3
	board.print_board()
	assert board.check_win() == True

Game()

board = Board()
board.board[0][1], board.board[1][1] = ['x'] * 2
board.board[0][0], board.board[0][2] = ['o'] * 2

stack = []
test_board = board
move = None
best = [None, 100000, 0] # position and length and tie or win

def allowable_spaces(board):
	spaces = []

	for row in range(len(board.board)):
		for col in range(len(board.board[0])):
			if board.board[row][col] == '-':
				spaces.append([row, col])

	return spaces

def some_fn(row_col):
	test_board[row_col[0]][row_col[1]] = player.marker
	stack.append(row_col)

	status = test_board.status()

	if status == None:
		some_fn(allowable_spaces.pop())
		# somehow make the player different
	else:
		if player.marker == 'x': # human
			if status > best[2]:
				if len(stack) < best[1]:
					best = [row_col, len(stack), status]
		elif player.marker == 'o': # computer
			if status < best[2]:
				if len(stack) < best[1]:
					best = [row_col, len(stack), status]			

	allowable_spaces.append(stack.pop())

allowable_spaces = allowable_spaces(board)[::-1]

while len(allowable_spaces) > 0:
	# init test_board
	test_board = board.board
	# init stack
	stack = []
	# init allowable_spaces
	some_fn(allowable_spaces.pop())

for row in range(len(test_board)):
	for col in range(len(row)):
		if test_board[row][col] == '-':
			some_fn(row, col)

			for row in range(len(test_board)):
				for col in range(len(row)):
					if test_board[row][col] == '-':
						test_board[row][col] = 'o'

for space in allowable_spaces(test_board):
	test_board[space[0]][space[1]] = 'x'
	some_fn(space[0], space[1])