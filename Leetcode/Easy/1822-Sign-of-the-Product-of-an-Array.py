class Solution:
    def arraySign(self, nums: List[int]) -> int:
        # Time: O(n)
        # Space: O(1)
        
        # Count the frequency of negative numbers
        negatives = 0
        
        for num in nums:
            if num == 0: return 0 # Edge case
            
            if num < 0: negatives += 1
        
        # Even negative frequency results in a positive result
        # while odd negative frequency results in a negative result
        return 1 if negatives % 2 == 0 else -1
        