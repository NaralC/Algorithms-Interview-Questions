from collections import Counter
from heapq import *

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        return bucketSort(nums, k)
        
def minimumHeap(nums, k):
    # Time: O(n + klogn)
    # Space: O(n + k)
    tracker = Counter(nums)

    # We use a min heap so least frequent elements rise to the top and we pop them later
    minHeap = [(freq, num) for num, freq in tracker.items()]
    heapify(minHeap)

    while len(minHeap) > k: heappop(minHeap)

    return [num for freq, num in minHeap]
        
def bucketSort(nums, k):
    # Time: O(n)
    # Space: O(n)
    # The most frequent a number can be is len(nums) -> Bucket Sort
    # So use buckets to indicate what numbers have x frequency

    # Get the frequency of each number with a hash table
    freq = Counter(nums)

    # Allocate buckets, each one indicating a frequency
    buckets = [[] for _ in range(len(nums) + 1)]

    for num in set(nums):
        buckets[freq[num]].append(num)

    # Return the top k most frequent elements
    output = []

    for idx in reversed(range(len(buckets))):
        if buckets[idx] != []:
            for num in buckets[idx]:
                output.append(num)

                if len(output) == k:
                    return output


    return output
