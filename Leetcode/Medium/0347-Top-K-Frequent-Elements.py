from collections import Counter
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        return maxHeap(nums, k)
        
def sortDict(nums, k):
    #Time: O(nlogn)
    #Space: O(n)

    #Map each number's frequency
    count = Counter(nums)

    #Sort the hash table by each number's frequency
    #The table will now be converted to a list of keys
    count = sorted(count, key = lambda x: count[x], reverse = True)

    return count[:k]
        
def maxHeap(nums, k):
    #Time: O(nlogk) popping out an element costs O(logn) and we have k elements to pop
    #Space: O(n)

    #Map each number's frequency
    count = Counter(nums)

    #Convert it into a list, so it works with heapify
    count = [(-freq, num) for num, freq in count.items()]
    heapq.heapify(count) #This turns into a max heap since freq of each num is negative

    #Ship the output
    output = []

    for _ in range(k):
        output.append(heapq.heappop(count)[1]) #Only append the number

    return output