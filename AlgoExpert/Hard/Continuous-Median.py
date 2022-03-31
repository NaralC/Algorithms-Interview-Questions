# Do not edit the class below except for
# the insert method. Feel free to add new
# properties and methods to the class.
from heapq import *

class ContinuousMedianHandler:
    def __init__(self):
        # maxHeap carries smaller numbers, while minHeap keeps larger numbers
		# To retrieve the median in constant time - simply take the top of each heap
		# Keep the size difference < 1
		
		#  maxHeap     minHeap      median
		# [1, 2, 4]   [5, 6, 7]    = [4, 5]
		self.maxHeap, self.minHeap = [], []

    def insert(self, number):
        # By default - add new numbers to maxHeap
		heappush(self.maxHeap, -number) # Invert the number to make this a max heap
		
		# In case we just assigned a larger number to maxHeap, take it back to minHeap
		if len(self.maxHeap) and len(self.minHeap) and -self.maxHeap[0] > self.minHeap[0]:
			heappush(self.minHeap, -heappop(self.maxHeap))
			
		# Adjust the heaps to keep the size difference < 1
		if len(self.maxHeap) - 1 > len(self.minHeap):
			heappush(self.minHeap, -heappop(self.maxHeap))
		elif len(self.minHeap) - 1 > len(self.maxHeap):
			heappush(self.maxHeap, -heappop(self.minHeap))

    def getMedian(self):
        # In case there are a total of odd numbers
		if len(self.maxHeap) > len(self.minHeap):
			return -self.maxHeap[0]
		elif len(self.minHeap) > len(self.maxHeap):
			return self.minHeap[0]
		
		# In case there are a total of even numbers
		return (-self.maxHeap[0] + self.minHeap[0]) / 2
