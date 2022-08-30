from collections import Counter
from heapq import *

class Solution:
    def minDeletions(self, s: str) -> int:
        return bruteForce(s) or maxHeap(s)

def bruteForce(s):
    # Time: O(n^26)
    # Space: O(n)

    # Keep deleting until the frequency is unique
    seenFreqs = set()
    delCount = 0

    for char, freq in Counter(s).items():
        # No negative frequencies allowed
        while freq in seenFreqs and freq > 0:
            freq -= 1
            delCount += 1

        seenFreqs.add(freq)

    return delCount
        
def maxHeap(s):
    # Time: O(nlogn)
    # Space: O(n)

    # Keep deleting until the frequency is unique
    delCount = 0
    maxHeap = [-freq for freq in Counter(s).values()]
    heapify(maxHeap)

    while len(maxHeap) >= 2:
        popped = -heappop(maxHeap)

        if popped == -maxHeap[0]:
            # No negative frequency allowed
            if popped > 1:
                heappush(maxHeap, -popped + 1)

            delCount += 1

    return delCount