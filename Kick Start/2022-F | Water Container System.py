# Kick Start 2022
# Round F
# Water Container System

from itertools import accumulate as acc, filterfalse as ff

def level(number, links, current = 1):
	# if number == 1:
	# 	return current
	# else:
	# 	parent = tuple(pair[0] for pair in links if pair[1] == number)[0]
	# 	# print(f'{number}\'s parent: {parent}')
	# 	current += 1
	# 	return level(parent, links, current)
	while number != 1:
		number = tuple(pair[0] for pair in links if pair[1] == number)[0]
		current += 1
	return current


def water():
	(N,Q) = map(int, input().split())

	links = set()
	for x in range(N-1):
		links.add(tuple(sorted(map(int, input().split()))))

	addAt = tuple()
	for y in range(Q):
		addAt += (int(input()),)

	volume = len(addAt)

	allLevels = tuple(level(x,links) for x in range(1,N+1)) # Level of each container
	allLevels = {x:allLevels.count(x) for x in allLevels} # Containers at each level
	full = max(ff(lambda r: r>volume, (acc(allLevels.values()))))
	# print(f'allLevels = {allLevels}')

	return full

if __name__ == '__main__':
	for case in range(1, int(input())+1):
		print(f'Case #{case}: {water()}')