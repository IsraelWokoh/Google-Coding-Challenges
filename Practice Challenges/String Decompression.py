# Former Interview Question
# Compression and Decompression
# https://techdevguide.withgoogle.com/resources/former-interview-question-compression-and-decompression/#!

def findBrackets(string): # Finds (innermost) []
	charIndex = dict() # DICT keys are unique - important

	for char in range(len(string)): # iterate over string indices
		charIndex[string[char]] = char # updates charIndex{} with the latest index of char
		if string[char] == ']': # At first closing bracket
			break # ends the loop

	return charIndex['['], charIndex[']'] # returns positions [ and ]

def findEnclosedText(string, start, end): # Finds substring in [substring]
	return string[start+1:end]

def findFDI(string, position): # Finds no. of repetitions, K, in K[substring]
	while True: # keep looping
		if string[position-1] not in '0123456789': # if not integer
			break # stop
		else:
			position -= 1 # Decrement = move backwards in string
	return position # returns index of first digit

def replaceString(string, firstDigitIndex, multiplier, end, text): # ...replacing K[substring] with K repetitions of substring
	return string[:firstDigitIndex] + multiplier * text + string[end+1:] # Adds fragments of text...

def decompress(string):
	step = 1

	while '[' in string: # While there are still compressed sections
		'''
		"Input is always valid", so I can check for just one type of bracket,
		since one's presence implies the other's.
		'''

		openingBracketIndex, closingBracketIndex = findBrackets(string) # Finds positions of first [] pair (with no other brackets between them)
		substring = findEnclosedText(string, openingBracketIndex, closingBracketIndex) # Finds substring inside first [] pair
		firstDigitIndex = findFDI(string, openingBracketIndex) # Finds position of leftmost digit (in a group of contiguous digits)
		multiplier = int(string[firstDigitIndex:openingBracketIndex]) # Finds multiplier as INT

		string = replaceString(
			string, firstDigitIndex,
			multiplier, closingBracketIndex,
			substring
		) # Performs substring replacement

		print(f'Step {step}: {string}\n')
		step += 1

	return string

if __name__ == '__main__':
	string = '3[abc]4[ab]6[qx2[u]]'
	print(f'Original string: {string}\n')
	print(f'Decompressed form: {decompress(string)}')
