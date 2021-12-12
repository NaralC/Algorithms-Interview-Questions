def sortedSquaredArray(array):
    temp = []
	for number in array:
		temp.append(pow(number, 2))
	
	temp.sort()
	return temp 