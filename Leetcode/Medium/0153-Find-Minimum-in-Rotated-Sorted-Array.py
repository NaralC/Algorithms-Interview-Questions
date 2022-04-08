class Solution:
    def findMin(self, nums: List[int]) -> int:
        # Time: O(logn)
        # Space: O(1)
        
        # Edge cases: if nums is already sorted, or has a length of 1
        if nums[0] <= nums[-1]:
            return nums[0]
        
        l, r = 0, len(nums) - 1
        
        while l <= r:
            mid = (l + r) // 2
            
            if nums[mid] > nums[mid + 1]:
                return nums[mid + 1]
        
            # Mid currently on the left side -> Go left til we find the minimum
            if nums[mid] >= nums[0]:
                l = mid + 1
            
            # Mid currently on the right side -> Go right til we find the minimum
            else:
                r = mid - 1
