from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Time: O(nlogn)
        # Space: O(n)

        # Map each number to freq
        freqMap = defaultdict(int)

        for num in nums:
            freqMap[num] += 1

        # Sort them by freq
        sortedByFreq = sorted(freqMap.items(), key = lambda x: x[1], reverse = True)

        return [num for num, _ in sortedByFreq][:k]


from heapq import *

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Time: O(nlogk), time complexity of heap push/pop is O(logk) - k being heap size
        # Space: O(n)

        # Map each number to freq
        freqMap = defaultdict(int)

        for num in nums:
            freqMap[num] += 1

        # Use max heap to screen for top k elements
        maxHeap = []

        # Heapq module is a min heap, so we're keeping the frequent numbers at the bottom
        for num, freq in freqMap.items():
            heappush(maxHeap, (freq, num))

            # This keeps the heap size to k, hence the time complexity being O(n * logk)
            if len(maxHeap) > k: 
                heappop(maxHeap)

        # Ship output
        output = []

        for _ in range(k):
            freq, num = heappop(maxHeap)
            output.append(num)

        return output
