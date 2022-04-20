class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        # Time: O(n)
        # Space: O(n)
        
        maxLength = 0
        zeroes = 0
        
        # Extend our window until we've encountered k zeroes
        start = 0
        
        while zeroes < k and start < len(nums):
            if nums[start] == 0:
                zeroes += 1
            
            start += 1
            maxLength = max(maxLength, start)
        
        # Continue the sliding window
        left = 0
        
        for right in range(start, len(nums)):
            if nums[right] == 0:
                zeroes += 1
            
            while zeroes > k:
                if nums[left] == 0: 
                    zeroes -= 1
                    
                left += 1
            
            maxLength = max(maxLength, right - left + 1)
        
        return maxLength