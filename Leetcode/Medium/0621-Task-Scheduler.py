class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # Time: O(n * log26) maxHeap with only English alphabets
        # Space: O(26)
        
        # Put each char's freq into maxHeap, with biggest freqs being on top
        frequencies = Counter(tasks)
        maxHeap = [-freq for freq in frequencies.values()]
        heapify(maxHeap)
        
        # Use up the most frequent chars first (from the heap)
        # And put them into the q, awaiting the next it becomes available (accounting the cooldown)
        time = 0
        q = deque() # holds (freq, time of availability)
        
        while len(q) or len(maxHeap):
            # Put the most freq chars into q
            if len(maxHeap):
                freq = -heappop(maxHeap) - 1 # Decrement the count
                
                if freq > 0:
                    q.append((-freq, time + n))
                
            # Use a char if it comes time
            if len(q) and q[0][1] == time:
                heappush(maxHeap, q.popleft()[0])
            
            time += 1
            
        return time