# Former Interview Question
# Flatten Iterators
# https://techdevguide.withgoogle.com/resources/former-interview-question-flatten-iterators/#!

if __name__ == '__main__':
	# Pre-defined arrays
	arr1 = iter([1, 2, 3])
	arr2 = iter([4, 5])
	arr3 = iter([6, 7, 8, 9])
	arr4 = iter([10])
	arr5 = iter([11,12,13,14,15])
	bigIterator = [arr1, arr2, arr3, arr4, arr5] # iterator of iterators

	while bigIterator != []:
		toRemove = []
		for thing in bigIterator:
			try:
				print(next(thing))
			except StopIteration:
				toRemove.append(thing)
		for obj in toRemove:
			bigIterator.remove(obj)