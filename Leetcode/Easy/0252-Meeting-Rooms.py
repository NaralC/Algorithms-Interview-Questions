class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        # Time: O(nlogn)
        # Space: O(1)
        
        intervals.sort()
        
        for idx in range(1, len(intervals)):
            left_end, right_start = intervals[idx - 1][1], intervals[idx][0]
            
            if left_end > right_start:
                return False
        
        return True