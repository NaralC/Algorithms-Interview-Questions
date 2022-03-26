from heapq import heapify, heappush, heappop, nlargest

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        #Time: O(nlogk)
        #Space: O(n)
        
        self.k = k
        self.nums = nums
        heapify(self.nums)
        
        #The description doesn't say that the cap to the number of elements in the heap has to be less than k
        while len(self.nums) > self.k:
            heappop(self.nums)
        
    def add(self, val: int) -> int:
        #Time: O(nlogk)
        #Space: O(1)
        
        heappush(self.nums, val)
        
        #The description doesn't say that the cap to the number of elements in the heap has to be less than k
        while len(self.nums) > self.k:
            heappop(self.nums)
        
        return self.nums[0]

# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)