from heapq import heapify, nlargest

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # Time: O(nlogk)
        # Space: O(1)
        heapify(nums)

        while len(nums) > k: heappop(nums)

        return nums[0]
