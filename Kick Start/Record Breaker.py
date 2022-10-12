# Kick Start 2022
# Session 3

def record():
	N = int(input()) # number of days
	V = tuple(map(int, input().split())) # number of visitors
	R = 0 # number of record-breaking days
	for Vi in range(len(V)):
		if not Vi or V[Vi] == max(V[:Vi+1]) \
				and V.count(max(V)) == 1:
			if Vi == len(V)-1 or V[Vi] > V[Vi+1]:
				R += 1
	return R

if __name__ == '__main__':
	for case_no in range(1, int(input()) + 1):
		print(f'Case #{case_no}: {record()}')