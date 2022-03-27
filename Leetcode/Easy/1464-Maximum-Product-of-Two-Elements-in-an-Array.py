import heapq

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        #Time: O(nlogk)
        #Space: O(1)
        #Retrieve the two biggest numbers
        
        minHeap = nums[:2]
        heapq.heapify(minHeap)
        
        for idx in range(2, len(nums)):
            if nums[idx] > minHeap[0]:
                heapq.heappushpop(minHeap, nums[idx])
        
        return (minHeap[0] - 1) * (minHeap[1] - 1)