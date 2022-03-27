import heapq

class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        return sorting(score)
        
def sorting(score):
    #Time: O(nlogn)
    #Space: O(n)

    #Sort the array based on score
    scoreTable = [(marks, idx) for idx, marks in enumerate(score)]
    scoreTable.sort(reverse = True)

    #Assign ranks back to the original idx
    for rank in range(len(scoreTable)):
        idx = scoreTable[rank][1]

        if rank == 0:
            score[idx] = 'Gold Medal'
        elif rank == 1:
            score[idx] = 'Silver Medal'
        elif rank == 2:
            score[idx] = 'Bronze Medal'
        else:
            score[idx] = str(rank + 1)

    return score

def maxHeap(score):
    #Time: O(nlogn) as we still have to pop everything out
    #Space: O(n)

    #Turn the input array into a max heap
    score = [(-s, idx) for idx, s in enumerate(score)]
    heapq.heapify(score)

    #Ship the output
    output = [None] * len(score)
    count = 1

    while len(score):
        _, idx = heapq.heappop(score)

        if count == 1:
            output[idx] = 'Gold Medal'
        elif count == 2:
            output[idx] = 'Silver Medal'
        elif count == 3:
            output[idx] = 'Bronze Medal'
        else:
            output[idx] = str(count)

        count += 1

    return output