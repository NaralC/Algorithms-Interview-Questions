from heapq import heappush, heapify

class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        #Time: O(k * logm) as we extract k numbers from a heap of size m; m = len(matrix)
        #Space: O(m)
        
        #Retrieve each array's tail
        minHeap = []
        
        for row in range(len(matrix)):
            minHeap.append((matrix[row][0], row, 0)) #This info helps us move on to the next value later on
        
        heapify(minHeap)
        
        #Ship the kth smallest number
        for _ in range(k):
            if _ == k - 1:
                return heappop(minHeap)[0]
        
            val, row, col = heappop(minHeap)
            
            #Push the next value of the list to heap it it's not the last
            if col < len(matrix[0]) - 1:
                heappush(minHeap, (matrix[row][col + 1], row, col + 1))