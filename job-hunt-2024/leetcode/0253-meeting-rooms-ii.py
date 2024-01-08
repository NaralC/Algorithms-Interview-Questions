class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        # Time: O(nlogn)
        # Space: O(n)

        # Form a chronological order of when meetings start and end
        timestamps = []

        for start, end in intervals:
            timestamps.append((start, 1)) # Demands a room
            timestamps.append((end, -1)) # Lets go of a room

        # Count the maximum number of concurrent meetings
        room, maxRoom = 0, 0
        
        for _, modifier in sorted(timestamps, key = lambda x: (x[0], x[1])):
            room += modifier
            maxRoom = max(maxRoom, room)

        return maxRoom
