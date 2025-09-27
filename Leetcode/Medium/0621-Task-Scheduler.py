from heapq import *
from collections import *

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # Time: O(nlogk)
        # Space: O(n)

        # Tracks and uses up *the most frequent* (and available) tasks first. We can ignore the letters
        maxHeap = [-freq for _, freq in Counter(tasks).items()]
        heapify(maxHeap)
        # Tracks tasks on cooldown to be eventually put back into the heap. Contains (readyWhen, freq)
        q = deque()
        time = 0
        
        while len(maxHeap) or len(q):
            # If tasks are ready in the q
            while len(q) and time >= q[0][0]:
                # Put them into the heap
                _, negFreq = q.popleft()
                heappush(maxHeap, negFreq)

            # Perform a task from the heap
            if len(maxHeap):
                posFreq = -heappop(maxHeap)
                posFreq -= 1

                # Put into q
                if posFreq:
                    q.append((time + n + 1, -posFreq))

            time += 1

        return time
        
