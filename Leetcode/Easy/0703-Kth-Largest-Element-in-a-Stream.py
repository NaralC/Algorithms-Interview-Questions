from heapq import *

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        # Time: O(n + klogn)
        # Space: O(k)
        
        # To get the kth largest, track the top k biggest with a min heap
        self.minHeap = nums
        heapify(self.minHeap)
        self.limit = k
        
        # Shave off smallest numbers - we only care about the k biggest ones
        while len(self.minHeap) > self.limit:
            heappop(self.minHeap)

    def add(self, val: int) -> int:
        # Time: O(logn)
        # Space: O(1)
        
        heappush(self.minHeap, val)
        
        # Shave off smallest numbers - we only care about the k biggest ones
        # In this case there is at most one extra since we have dealt with smallest ones when initializing
        if len(self.minHeap) > self.limit:
            heappop(self.minHeap)
        
        return self.minHeap[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)