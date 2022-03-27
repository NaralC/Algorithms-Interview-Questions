import heapq

class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        return priorityQueue(mat, k)
        
def bruteForce(mat, k):
    #Time: O(m * logn + mlogm) as we perform binary search over m rows
    #Time: O(k)

    #Initialize our array to track the soldier count of each row
    soldiers = [None] * len(mat)

    for idx in range(len(mat)):
        soldiers[idx] = (countSoldiers(mat[idx]), idx) #Utilize binary seach to find the last appearance of 1

    #Sort the row by soldier count
    soldiers.sort(key = lambda x: (x[0], x[1]))

    #Ship the output
    return [soldiers[idx][1] for idx in range(k)]
        
def priorityQueue(mat, k):
    #Time: O(m * (logn + logk))
    #Space: O(k)

    #Keep strong rows on top, weak rows at the bottom
    maxHeap = []
    heapq.heapify(maxHeap)

    for idx, row in enumerate(mat):
        #Calculate each row's strength with binary search
        info = [-countSoldiers(row), -idx]

        #Append to heap if there's space or current row is stronger than top most row in heap
        if len(maxHeap) < k or info > maxHeap[0]:
            heapq.heappush(maxHeap, info)

        #Pop out if there are more than k elements
        if len(maxHeap) > k:
            heapq.heappop(maxHeap)

    #Ship the output
    output = []

    for _ in range(k):
        idx = heapq.heappop(maxHeap)[1]
        output.append(-idx)

    return output[::-1]
        
def countSoldiers(row):
    #Time: O(logn)
    #Space: O(1)
    
    left, right = 0, len(row) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        if row[mid] == 0:
            right = mid - 1
        else:
            left = mid + 1
    
    return left