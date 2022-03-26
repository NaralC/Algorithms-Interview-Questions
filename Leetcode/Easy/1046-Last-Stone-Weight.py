from heapq import heapify, heappop, heappush

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        #Time: O(nlogn) as we pop from heap n times
        #Space: O(n)
        
        #Invert the weights to turn them into a max heap
        stones = [-weight for weight in stones]
        heapify(stones) #since heaps in Python are min heaps by default
        
        #Pop the top 2 heaviest stones
        while len(stones) >= 2:
            s1 = -(heappop(stones))
            s2 = -(heappop(stones))
            
            #Both stones are of equal weight -> Both get destroyed
            if s1 == s2:
                continue
            
            #s1 is heavier -> Append the remaining weight back to heap
            else:
                heappush(stones, -(s1 - s2))
        
        return -(stones[0]) if len(stones) else 0