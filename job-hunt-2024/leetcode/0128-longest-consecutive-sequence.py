class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Time: O(n)
        # Space: O(n)

        if not len(nums): return 0

        longest = 1
        seen = set(nums)

        for num in nums:
            # Check if this is the start of a sequence
            if num - 1 not in seen:
                cur = 1

                while num + cur in seen:
                    cur += 1
                
                longest = max(longest, cur)
            
        return longest
