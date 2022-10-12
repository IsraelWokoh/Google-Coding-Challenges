# Kick Start 2022
# Round F
# Story of Seasons

from itertools import filterfalse as ff
from operator import itemgetter

def seasons():
	(D,N,X) = map(int, input().split()) # Days | no. of seed types | Max plants per day
	print(f'D: {D}\nN: {N}\nX: {X}')

	seeds = []
	for i in range(1, N+1): # Getting all seed data
		[Qi,Li,Vi] = map(int, input().split()) # Quantity, Life (to maturity), Value (at maturity)
		print(f'Q{i}: {Qi} | L{i}: {Li} | V{i}: {Vi}')
		seeds.append([Qi,Li,Vi])
	# print(f'Seeds: {seeds}')

	profit = 0
	for j in range(1, D+1): # for each day
		# print(f'\n-----DAY {j}-----')
		seeds = ff(lambda seed: seed[1]+j > D, seeds) # filter out seeds with overly long maturity
		for k in range(1,X+1): # Up to max plants per day
			# print(f'+++Plant {k}+++')
			seeds = sorted(
				ff(lambda s: not s[0], seeds), # filter out zero quantity
				key=itemgetter(1,2),
				reverse=True
			)
			# print(seeds)
			if seeds != []:
				profit += seeds[0][2]
				# print(profit)
				seeds[0][0] -= 1

	return profit

if __name__ == '__main__':
	for case in range(1, int(input())+1):
		print(f'Case #{case}: {seasons()}\n')