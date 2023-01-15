from collections import Counter
from heapq import *

class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        # Time: O(nlogn)
        # Space: O(n)

        # Greedy, remove the chars with the lowest counts first
        arr = [(freq, char) for char, freq in Counter(arr).items()]
        arr.sort(reverse = True)

        # (freq, element)
        # [(2, 5), (1, 4)] 
        # [(3, 3), (2, 1), (1, 4), (1, 2)]
        while k > 0:
            if arr[-1][0] <= k:
                k -= arr[-1][0]
                arr.pop()
            else:
                break

        return len(arr)
        