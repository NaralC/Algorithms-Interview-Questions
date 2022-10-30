from heapq import *

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        return timestamps(intervals)
        # return priorityQueue(intervals)
        
def timestamps(intervals):
    # Time: O(nlogn)
    # Space: O(n)

    # Categorize all timestamps
    timestamps = []
    
    for start, end in intervals:
        timestamps.append((start, 'start'))
        timestamps.append((end, 'end'))
        
    timestamps.sort()

    # Operate on a basis that:
    # - if a meeting starts, allocate one more room
    # - if a meeting ends, free one room
    room_usage = output = 0
    
    for time, info in timestamps:
        if info == 'start':
            room_usage += 1
        else:
            room_usage -= 1 if room_usage > 0 else 0
            
        output = max(output, room_usage)

    return output

def priorityQueue(intervals):
    # Time: O(nlogn)
    # Space: O(n)

    # Push every timestamp into a min heap
    minHeap = [] # (time, start/end)

    for start, end in intervals:
        heappush(minHeap, (start, 'start'))
        heappush(minHeap, (end, 'end'))

    # Operate on a basis that:
    # - if a meeting starts, allocate one more room
    # - if a meeting ends, free one room
    room_usage = output = 0

    while len(minHeap):
        time, info = heappop(minHeap)

        if info == 'start':
            room_usage += 1

        else:
            room_usage -= 1 if room_usage > 0 else 0

        output = max(output, room_usage)

    return output
    