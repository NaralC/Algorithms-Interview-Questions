def twoNumberSum(array, targetSum):
    seen = set()
	
	for num in array:
		diff = targetSum - num
		
		if diff in seen:
			return [diff, num]
		seen.add(num)
	
	return []