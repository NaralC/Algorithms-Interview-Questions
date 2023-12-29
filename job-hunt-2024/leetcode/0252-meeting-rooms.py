class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        # Time: O(nlogn)
        # Space: O(n)

        if len(intervals) == 0: return True

        intervals.sort(key = lambda x: x[0]) # Sort by starting time
        cur = intervals[0]
        
        for start, end in intervals[1:]:
            # See if start overlaps with current ending
            if cur[1] > start:
                return False
            
            # Merge into one
            cur = [min(start, cur[0]), max(end, cur[1])]
        
        return True
        