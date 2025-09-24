from heapq import *

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # Time: O(n * logk) since we iterate through everything, while pushing to a heap costs O(log * heapSize)
        # Space: O(k)
        
        maxHeap = []

        for x, y in points:
            distance = -getDistance(x, y) # max heap since we want to keep smaller values
            heappush(maxHeap, (distance, [x, y]))

            while len(maxHeap) > k:
                heappop(maxHeap) # push out largest values

        return [coordinates for distance, coordinates in maxHeap]
    
def distance(x, y):

    return sqrt((x - 0) ** 2 + (y - 0) ** 2)
