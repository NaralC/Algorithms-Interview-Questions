def isValidSubsequence(array, sequence):
	subPtr = 0
	for number in array:
		if number == sequence[subPtr]:
			subPtr += 1
		if subPtr > len(sequence) - 1:
			return True
	
	return False