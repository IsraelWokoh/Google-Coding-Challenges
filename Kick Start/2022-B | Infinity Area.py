# Google Kick Start
# 2022: Round B
# Infinity Area

from math import pi

def area():
	(R,A,B) = map(int, input().split())
	total = 0
	step = 0
	while R:
		total += pi*R**2
		R = R*A if not step%2 else R//B
		step += 1
	return total

if __name__ == '__main__':
	for case in range(1, int(input())+1):
		print(f'Case #{case}: {area()}')