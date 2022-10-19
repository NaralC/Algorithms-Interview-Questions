from collections import defaultdict

class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        # Time: O(n)
        # Space: O(n)
        
        lookup = defaultdict(int) # { prefix_sum : count }
        lookup[0] = 1 # because [5], [5, 0] both count
        cur_sum = output = 0
        
        for num in nums:
            cur_sum += num
            cur_sum %= k
            
            output += lookup[cur_sum]
            lookup[cur_sum] += 1
        
        return output
    