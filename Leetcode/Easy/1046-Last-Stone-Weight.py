from heapq import *

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # Time: O(n * logn) as we pop out all the stones, each time costing O(logn)
        # Space: O(n)
        
        # Invert the values so that we get a max heap
        stones = [-s for s in stones]
        heapify(stones)
        
        # Begin comparing 2 heaviest stones
        while len(stones) >= 2:
            s1 = -heappop(stones)
            s2 = -heappop(stones)
            
            if s1 > s2:
                heappush(stones, -(s1 - s2))
        
        return -stones[0] if len(stones) else 0