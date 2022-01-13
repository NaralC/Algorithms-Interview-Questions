class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        #Time: O(nlogn)
        #Space: O(1)
        #The idea is the same is 'Minimum Number of Arrows to Burst Balloons' but a few modifications
        
        intervals.sort(key = lambda x: x[0])
        
        prevEnd = intervals[0][1]
        count = 0
        
        for currentStart, currentEnd in intervals[1:]:
            #Overlap - keep the smaller one (greedy)
            if prevEnd > currentStart:
                count += 1
                prevEnd = min(prevEnd, currentEnd)
            
            #No overlap - proceed to the next one
            else:
                prevEnd = currentEnd
            
        return count