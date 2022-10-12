# Kick Start 2022
# Session 3

from operator import add

def walk(position, direction):
	change = {
		'N':(-1,0),
		'E':(0,1),
		'S':(1,0),
		'W':(0,-1)
	}
	return tuple(map(add, position, change[direction]))

def wiggle():
	(N, R, C, Sr, Sc) = tuple(map(int, input().split()))
	route = input() # set of directions
	seen = set() # all visited points
	position = (Sr, Sc) # starting position
	seen.add(position)
	for move in route: # for each move in route
		unseen = False
		while not unseen: # while new position not visited yet
			newPosition = walk(position, move)
			if newPosition not in seen:
				unseen = True # found new position
				seen.add(newPosition)
			position = newPosition
	return f'{position[0]} {position[1]}' # return end point


if __name__ == '__main__':
	for case_no in range(1, int(input()) + 1):
		print(f'Case #{case_no}: {wiggle()}')