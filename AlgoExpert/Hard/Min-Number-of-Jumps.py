def minNumberOfJumps(array):
    #Time: O(m^n) where m = max(nums), n = len(array)
	#Space: O(m^n)
	def traverse(currentPos):
		if currentPos >= len(array) - 1:
			return 0
		
		count = float('inf')
		for leap in range(1, array[currentPos] + 1):
			count = min(count, 1 + traverse(currentPos + leap))
			
		return count
	
	#Time: O(n)
	#Space: O(1)
	def greedy():
		count = 0
		left, right = 0, 0
		
		while right < len(array) - 1:
			maxLeap = 0
			
			for leap in range(left, right + 1):
				maxLeap = max(maxLeap, leap + array[leap])
			
			left = right + 1
			right = maxLeap
			count += 1
		
		return count
	
	#Pick your algorithm here
	return greedy()