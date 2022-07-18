# Kick Start 2022
# Round B
# Palindromic Numbers

from math import sqrt # Could also raise to power of 0.5, but I think this was slightly faster...?

def palindromic(number):
	for x in range(len(number)//2 + 1): # Up to halfway
		if number[x] != number[-(x+1)]: # equates first and last, working inwards
			return False # NOT palindromic
	return True # palindromic

if __name__ == '__main__':
	end = int(input()) # Test Set A: 1000; B: 10^10 - is Python too slow for that?

	for dividend in range(1, end + 1):
		pdCount = 0 # Number of palindromic factors, for each dividend

		for divisor in range(1, int(sqrt(dividend)) + 1): # incremented up to sqrt(dividend)
			if not dividend % divisor: # if remainder == 0 <=> if factor

				for each in {divisor, dividend // divisor}: # checks divisor and quotient
                    # Using a set handles perfect square division; {x, x**2//x} = {x}
					if palindromic(str(each)): # if palindromic
						pdCount += 1 # increment palindrome counter

		print(f'Case #{dividend}: {pdCount}')
