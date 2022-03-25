from collections import Counter
import heapq

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        return maxHeap(words, k)
        
def sortDict(words, k):
    #Time: O(nlogn)
    #Space: O(n)

    #Map down each word's frequency
    count = Counter(words)
    count = [(-freq, word) for word, freq in count.items()]

    #Sort the words with frequency followed by lexicography
    #Since the freq is inverted, most frequent elements come first
    count = sorted(count, key = lambda x: (x[0], x[1]))
    count = [word for _, word in count]

    return count[:k]
    
def maxHeap(words, k):
    #Time: O(nlogk)
    #Space: O(n)

    #Map each word's frequency into a hash table
    count = Counter(words)

    #Convert to max heap since the smallest val goes on top (inverted freq in this case)
    count = [(-freq, word) for word, freq in count.items()] 

    #heapify takes care of the lexicographical order subtly - two heaps are automatically for freq and word
    heapq.heapify(count)

    #Pop out the most frequent k elements
    return [heapq.heappop(count)[1] for _ in range(k)]