from collections import Counter

class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        # Time: O(n)
        # Space: O(n)
        
        # Find numbers that represent the degree
        lookup = Counter(nums)
        deg = max(lookup.values())
        most_freq = set()
        
        for num in nums:
            if lookup[num] == deg:
                most_freq.add(num)
                
        # Find the length of subarray[l:r+1] where
        # l = first occurence of most frequent element
        # r = last occurence of most frequent element
        # since all occurences of most frequent element are in there, equalizing the degree
        output = float('inf')
        
        for candidate in most_freq:
            l = 0; r = len(nums) - 1
            
            while l < len(nums):
                if nums[l] == candidate: break
                l += 1
                
            while r > -1:
                if nums[r] == candidate: break
                r -= 1
                
            output = min(output, r - l + 1)
        
        return output
    