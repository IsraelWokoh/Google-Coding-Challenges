# Former Interview Question
# Volume of Lakes
# https://techdevguide.withgoogle.com/resources/former-interview-question-volume-of-lakes/#!

def trim(heights): # Truncates both ends of heights[] with area 0
	if heights != []:
		for x in range(2):
			index = 0

			while index < len(heights) - 1:
				if heights[index + 1] < heights[index]: # if downwards slope
					break # Stopping point for deletion
				index += 1

			# Flipped: happens twice, so retains normal orientation
			heights = list(reversed(heights[index:]))
	else:
		heights = [0]
	return heights

def shorten(heights): # Any solitary maximum value is brought down to next tallest
	maxSize = max(heights)
	if not maxSize: # if max height is 0
		return False

	if heights.count(maxSize) == 1: # if solitary
		index = heights.index(maxSize)
		heights[index] -= 1 # decrement
		return shorten(heights) #
	else:
		return heights

def findEnd(heights): # Determine end point for addToArea inner iteration
	for ind in range(1, len(heights)):
		if heights[-ind] == max(heights): # working backwards
			return len(heights) - ind # returns complement

def addToArea(heights, total = 0):
	for maxHeight in range(max(heights), -1, -1): # Working from tallest height downwards
		end = findEnd(heights)  # Find end point of index iteration

		# from first index of current height, to last index of max height
		for index in range(heights.index(maxHeight), end):
			if heights[index] < maxHeight: # If ground is lower (if water can occupy that area)
				total += 1 # increment total area

		# shave down tallest heights by 1 - eventually levels out
		heights = [x if x != max(heights) else max(heights) - 1 for x in heights]
	return total

def trappedArea(heights): # Overall function
	print(f'Heights: {heights}')
	heights = shorten( # Reduces tallest height if solitary
		trim(heights) # Trims ends without area
	)
	print()

	if not heights:
		print(f'No volume of trapped water could be found.')
	else:
		print(f'Total volume of trapped water: {addToArea(heights)}')

if __name__ == '__main__':
	heights = [
		1, 3, 2, 4,
		1, 3, 1, 4,
		5, 2, 2, 1,
		4, 2, 2
	]
	trappedArea(heights)
