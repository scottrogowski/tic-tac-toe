avail_spaces = avail_spaces()
stack = []

figure out whose turn it is

x = avail_spaces.pop()
player.move(x) # possible to pop the first one?
stack.append(x)

if board.status() == 1:
	if player.marker == 'x':
		best.append((stack[0], len(stack)))
	else:
		stack.pop()
		computer.move(avail_spaces[0])