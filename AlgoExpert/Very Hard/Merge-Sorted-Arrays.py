from heapq import *

def mergeSortedArrays(arrays):
	# Time: O(nlogm) where n = total number of numbers, m = number of lists
	# Space: O(n + m)
	
    # Grab the tail of each list
	minHeap = []
	
	for row in range(len(arrays)):
		# This info lets us proceed to next number in the list
		heappush(minHeap, (arrays[row][0], row, 0))
	
	# Use the heap to form a sorted list
	output = []
	
	while len(minHeap):
		num, row, col = heappop(minHeap)
		
		# Append to output
		output.append(num)
		
		# Move on to the next number in the list
		if col < len(arrays[row]) - 1:
			heappush(minHeap, (arrays[row][col + 1], row, col + 1))
	
	return output