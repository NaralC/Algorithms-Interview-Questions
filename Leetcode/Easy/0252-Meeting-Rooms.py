class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        #Time: O(nlogn)
        #Space: O(n)
        #No overlap in time intervals -> return True
        #If there's an overlap -> return False
        
        if not len(intervals): return True
        
        intervals.sort(key = lambda x: x[0])
        stack = [intervals[0]]
        
        for i in intervals[1:]:
            previousEnd = stack[-1][1]
            
            if previousEnd > i[0]:
                return False
            stack.append(i)
        
        return True