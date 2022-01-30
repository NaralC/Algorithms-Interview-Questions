class Solution:
    def search(self, nums: List[int], target: int) -> int:
        #Time: O(logn)
        #Space: O(1)
        
        left, right = 0, len(nums) - 1
        
        while left <= right:
            mid = (left + right) // 2
            candidate = nums[mid]
            
            if candidate > target:
                right -= 1
            elif candidate < target:
                left += 1
            else:
                return mid
        
        return -1