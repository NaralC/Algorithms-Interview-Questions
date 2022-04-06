from heapq import *

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # Time: O(n * logk) since we iterate through everything, while pushing to a heap costs O(log * heapSize)
        # Space: O(k)
        
        maxHeap = []
        
        for x, y in points:
            heappush(maxHeap, (- distance(x, y), [x, y])) # Make the heap sort the coordinates by their distance
            
            if len(maxHeap) > k:
                heappop(maxHeap)
        
        return [c for d, c in maxHeap]
    
def distance(x, y):
    return sqrt((x - 0) ** 2 + (y - 0) ** 2)