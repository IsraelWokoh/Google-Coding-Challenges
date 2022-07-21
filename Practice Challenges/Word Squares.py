# Former Interview Question
# Word Squares
# https://techdevguide.withgoogle.com/resources/former-interview-question-word-squares/#!

from itertools import combinations, permutations

def findWS(words):
	wordSquares = set() # To contain all word squares

	for combo in combinations(words, 4): # iterate over each 4-word sub-list
		for arr in permutations(combo): # and each permutation of that sublist
			if all(
					[arr[x] == # horizontal word matches
					 ''.join([word[x] for word in arr]) # corresponding vertical word
					 for x in range(len(arr))] # at each index
			):
				wordSquares.add(arr) # Store
				# print(f'#{len(wordSquares)}: {arr} qualifies!') # Notification
				break # *Might* be premature.

				# Intuition: sub-lists with palindromic words may present edge cases...
				# ...where sub-list CAN be rearranged. Untested, though.

	# Output
	print(f'No. of word squares contained: {len(wordSquares)}\n')
	for num, ws in enumerate(wordSquares, 1):
		print(f'#{num}: {ws}')

if __name__ == '__main__':
	words = ('AREA', 'BALL', 'DEAR', 'LADY', 'LEAD', 'YARD')
	findWS(iter(words))

	# Perhaps instead of finding squares, I could construct them...