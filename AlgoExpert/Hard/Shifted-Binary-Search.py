def shiftedBinarySearch(array, target):
	#Time: O(logn)
	#Space: O(1)
    #Find the pivot point -> pick a side to search
	
	def findMin(left, right):
		
		while left <= right:
			mid = (left + right) // 2
			
			#Found the dip
			if array[mid] > array[mid + 1]:
				return mid + 1
			
			#Mid is in the left portion (<= because mid could be on top of left)
			if array[0] <= array[mid]:
				left = mid + 1
			
			#Mid is in the right portion
			else:
				right = mid - 1
				
	def binarySearch(left, right):
		
		while left <= right:
			mid = (left + right) // 2
			
			if array[mid] == target:
				return mid
			
			if array[mid] < target:
				left = mid + 1
			else:
				right = mid - 1
		
		return -1
	
	
	#If the array is already sorted or has a length of 1, search the entire array
	if array[0] <= array[-1]:
		return binarySearch(0, len(array) - 1)
	
	#Retrieve where the rotation starts, a.k.a the minimum value
	pivot = findMin(0, len(array) - 1)
	
	#Pick a side to search
	#Search left if the left most element is <= to the target
	if array[0] <= target: #(<= because mid could be on top of left)
		return binarySearch(0, pivot - 1)
	
	#Else, search right
	else:
		return binarySearch(pivot, len(array) - 1)