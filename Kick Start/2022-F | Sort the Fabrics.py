# Kick Start
# 2022: Round F
# Sort the Fabrics

from operator import itemgetter

def tryInt(word):
	try:
		return int(word)
	except ValueError:
		return word

def sortFabric():
	fabrics = tuple()
	for fab in range(1, int(input())+1): # no. of fabrics
		(Ci, Di, Ui) = map(tryInt, input().split()) # colour, durability, ID
		fabrics += ((Ci, Di, Ui),)

	fabrics = sorted(fabrics, key = itemgetter(0,2)) # sorted by colour
	fabrics2 = sorted(fabrics, key = itemgetter(1,2)) # sorted by durability

	count = 0 # Same position counter
	for fabric in fabrics:
		count \
			+= fabrics.index(fabric) \
			== fabrics2.index(fabric)
	return count

if __name__ == '__main__':
	for case in range(1, int(input())+1):
		print(f'Case #{case}: {sortFabric()}')