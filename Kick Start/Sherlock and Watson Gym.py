# Kick Start 2022
# Session 3
# https://codingcompetitions.withgoogle.com/kickstart/round/00000000008f49d7/0000000000bcf0aa

from itertools import permutations as perms

def mod(pair, K):
	return (pair[0]%K, pair[1]%K)

def sprout():
	(A,B,N,K) = map(int, input().split())
	y = 0
	A %= K
	B %= K
	pairs = perms(range(1,N+1), 2)
	# pairs = set(map(mod, pairs, iter(K for pair in pairs)))
	memo = dict()
	'''
	{(11,2) -> y-value}
	'''
	for pair in pairs:
		pair = mod(pair,K)
		if mod(pair,K) not in memo:
		# if pair not in memo:
			memo[pair] = (pair[0]**(A**K) + pair[1]**(B**K))%K
		y += not memo[pair]

	# for i in range(1, N+1):
	# 	i %= K
	# 	i_A = i**A
	# 	for j in range(1, N+1):
	# 		j %= K
	# 		j_B = j**B
	# 		y += not (i_A + j_B) % K \
	# 			if i != j else 0
	return y%(10**9+7)

if __name__ == '__main__':
	for case in range(1, int(input())+1):
		print(f'Case #{case}: {sprout()}')