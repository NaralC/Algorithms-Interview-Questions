class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        #Time: O(n)
        #Space: O(1)
        
        longest, current = 0, 0
        
        for num in nums:
            if num == 1:
                current += 1
            else:
                longest = max(longest, current)
                current = 0
        
        return max(longest, current)