from heapq import *

class MedianFinder:

    def __init__(self):
        # maxHeap holds smaller numbers, while minHeap holds larger numbers,
        # so we can retrieve the top of each heap and return them as the median in constant time
        # The size difference must be < 1
        
        # maxHeap      minHeap     median
        #[1, 2, 3] -> [3, 4 ,5] -> [3, 3]
        self.maxHeap, self.minHeap = [], []

    def addNum(self, num: int) -> None:
        # Push to maxHeap by default
        heappush(self.maxHeap, -num)
        
        # In case we just handed a larger number to maxHeap, give it back to minHeap
        heappush(self.minHeap, -heappop(self.maxHeap))
        
        # Rebalance the heap if needed
        if len(self.maxHeap) - 1 > len(self.minHeap):
            heappush(self.minHeap, -heappop(self.maxHeap))
        elif len(self.maxHeap) < len(self.minHeap) - 1:
            heappush(self.maxHeap, -heappop(self.minHeap))

    def findMedian(self) -> float:
        # Odd case, return the extra number as median
        if len(self.maxHeap) > len(self.minHeap):
            return -self.maxHeap[0]
        elif len(self.maxHeap) < len(self.minHeap): 
            return self.minHeap[0]
        
        # Even case, return tops of both heaps as median
        return (-self.maxHeap[0] + self.minHeap[0]) / 2
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()