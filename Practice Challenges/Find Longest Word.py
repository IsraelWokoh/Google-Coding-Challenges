# Former Interview Question
# Find Longest Word
# https://techdevguide.withgoogle.com/resources/former-interview-question-find-longest-word/#!

def lettersAvailable(S, w): # checks if all letters available in S
	return all([w.count(letter) <= S.count(letter) for letter in w]) # checks abundance of characters

def inSequence(S, W): # checks if letters are in correct sequence
	reducedString = ''.join([char for char in S if char in W]) # deletes unnecessary characters from S
	charPositions = {char:reducedString.index(char) for char in W} # {char: its FIRST appearance}
	return sorted(charPositions.values()) == list(charPositions.values()) # Check for correct order

def largestSub(S, D): # finding largest valid subsequence
	D = sorted(
		[W for W in D if lettersAvailable(S, W)], # remove words without required letters
		key = len, # sorting by length...
		reverse = True # ...in descending order
	)

	for W in D: # for each word
		if inSequence(S, W): # if letters are in sequence
			return W # Returns largest because of earlier sorting

	# If no eligible words, or letters in wrong order
	print('No word was a subsequence of S')
	return "<NONE FOUND!>"

if __name__ == '__main__':
	S = 'abppplee'
	D = ["able", "ale", "apple", "bale", "kangaroo"]
	print(f'String: \'{S}\'')
	print(f'Words: {str(D)[1:-1]}')
	print(f'Longest available subsequence: {largestSub(S, D)}')
