from collections import defaultdict
from heapq import *

class Solution:
    def highFive(self, items: List[List[int]]) -> List[List[int]]:
        # Time: O(nlogn)
        # Space: O(n)
        # where n = len(items)
        
        # Hashtable + Max Heap
        # {1 : maxHeap(5, 1, 4, 5, 1)}
        
        lookup = defaultdict(list)
        
        for studId, score in items:
            heappush(lookup[studId], score)
            
            if len(lookup[studId]) > 5:
                heappop(lookup[studId])
        
        # Ship the output
        output = []
        
        for studId, scores in lookup.items():
            output.append([studId, sum(scores) // 5])
        
        return sorted(output, key = lambda x: x[0])