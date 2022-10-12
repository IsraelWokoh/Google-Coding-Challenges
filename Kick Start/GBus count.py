# Kick Start 2022
# Session 3

def GBus():
	N = int(input()) # No. of buses
	R = tuple(map(int, input().split())) # bus routes
	P = int(input()) # No. of cities to check
	C = '' # Output
	for bus in range(P):
		count = 0
		Ci = int(input())
		for b in range(N):
			count += int(Ci in range(R[2*b], R[2*b+1]+1))
		C += f'{str(count)} '
	return C.strip()

if __name__ == '__main__':
	T = int(input())
	for case in range(1, T + 1): # number of cases
		print(f'Case #{case}: {GBus()}')
		if T-case:
			blank = input()