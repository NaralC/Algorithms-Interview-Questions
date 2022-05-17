import heapq

class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        # Time: O(nlogn)
        # Space: O(n)
        
        # Sort events by starting date
        events.sort(reverse = True)
        
        # Determine boundary (jump to the first day)
        start = min(e[0] for e in events)
        end = max(e[1] for e in events)
        
        # Start here
        minHeap = [] # For keeping track of earliest-ending events
        output = 0 # Max number of events attendable
        
        for today in range(start, end + 1):
            
            # Push today's attendable events into the heap
            while len(events) and today == events[-1][0]:
                heapq.heappush(minHeap, events.pop()[1]) # Only push the ending dates
            
            # Discard past events
            while len(minHeap) and today > minHeap[0]:
                heapq.heappop(minHeap)
                
            # Pick the event that ends the earliest
            if len(minHeap):
                heapq.heappop(minHeap)
                output += 1
                
        return output