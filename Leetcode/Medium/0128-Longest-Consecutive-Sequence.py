class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #Time: O(n)
        #Space: O(n)
        
        nums.sort()
        longest = 0
        seen = set(nums)
        
        for num in nums:
            #See it the current number could be a start to a sequence
            if num - 1 not in seen:
                length = 1
                
                #Keep going to see how long the sequence is
                while num + length in seen:
                    length += 1
                
                #Update our variable
                longest = max(longest, length)
        
        return longest