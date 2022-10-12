# Kick Start 2022
# Session 3

def test():
	(N, M) = tuple(map(int, input('No. of bags and kids: ').split()))
	C = tuple(map(int, input('Candies in each bag: ').split()))
	return sum(C) % M


if __name__ == '__main__':
	for case in range(1, int(input('Enter number of cases: ')) + 1):
		print(f'Case #{case}: {test()}')