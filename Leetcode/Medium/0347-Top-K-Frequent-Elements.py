from collections import Counter
from heapq import *

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        return maxHeap(nums, k)
        
def maxHeap(nums, k):
    # Time: O(klogn)
    # Space: O(n)

    # Count the frequency of each number with a hash table
    freq = Counter(nums)

    # Let the heap sort the numbers by their frequencies
    nums = [(appearance, num) for num, appearance in freq.items()]
    heapify(nums)

    # Return top k most frequent elements
    return [num for _, num in nlargest(k, nums)]
        
def bucketSort(nums, k):
    # Time: O(n)
    # Space: O(n)
    # The most frequent a number can be is len(nums) -> Bucket Sort

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