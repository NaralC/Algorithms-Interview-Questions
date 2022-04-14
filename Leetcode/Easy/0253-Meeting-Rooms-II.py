class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        # Time: O(nlogn)
        # Space: O(n)
        # Find the max number of overlapping meetings
        
        # Retrieve the timestamps of when rooms are needed
        timestamps = []
        
        for start, end in intervals:
            timestamps.append((start, 1)) # Require one more room
            timestamps.append((end, -1)) # Require one less room
        
        timestamps.sort()
        
        # Go through the timestamp chronologically
        output = 0
        cur = 0
        
        for _, change in sorted(timestamps):
            cur += change
            output = max(output, cur)
        
        return output