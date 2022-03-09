def searchForRange(array, target):
	#Time: O(logn)
	#Space: O(1)
	
	def binarySearch(find, left = 0, right = len(array) - 1):
		found = False
		
		while left <= right:
			mid = (right + left) // 2
			candidate = array[mid]
			
			if candidate > target:
				right = mid - 1
			elif candidate < target:
				left = mid + 1
			else:
				found = True
				
				#Look for the first occurence of the target
				if find == 'start':
					right = mid - 1

				#Look for the last occurence of the target
				elif find == 'end':
					left = mid + 1
		
		if not found:
			return -1
		
		return left if find == 'start' else right
    
	return [binarySearch('start'), binarySearch('end')]