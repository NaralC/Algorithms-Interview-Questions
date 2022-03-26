from heapq import heapify, nsmallest

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        #Time: O(nlogk)
        #Space: O(k)
        
        #Append distances from (0,0) and coordinates
        minHeap = [(distance(c), c) for c in points]
        
        #Heapify this so smaller values are on top as it is min heap by default in Python
        heapify(minHeap)
        
        #Ship the k closest coordinates
        return [c for d, c in nsmallest(k, minHeap)]
    
def distance(coordinates):
    x, y = coordinates
    
    #No need to sqrt since a bigger number's gonna be bigger regardless of sqrt
    return pow(x, 2) + pow(y, 2)