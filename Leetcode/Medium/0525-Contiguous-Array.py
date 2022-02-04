class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        #Time: O(n)
        #Space: O(n)
        
        longest, count = 0, 0
        last_seen = {0: -1}
        
        for idx, num in enumerate(nums):
            
            count += 1 if num == 1 else -1
            
            if count in last_seen.keys():
                longest = max(longest, idx - last_seen[count])
            else:
                last_seen[count] = idx
            
        return longest