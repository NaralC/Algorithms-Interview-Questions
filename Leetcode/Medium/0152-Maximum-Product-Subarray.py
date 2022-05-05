class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # Time: O(n)
        # Space: O(1)
        # Use zeroes to divide subarrays
        
        output = float('-inf')
        left = right = 1
        
        for idx in range(len(nums)):
            if not left: left = 1
            if not right: right = 1
            
            left *= nums[idx]
            right *= nums[len(nums) - idx - 1]
            output = max(output, left, right)
            
        return output