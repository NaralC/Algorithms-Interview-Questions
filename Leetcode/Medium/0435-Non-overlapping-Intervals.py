class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        #Time: O(nlogn)
        #Space: O(1)
        
        #1) Sort intervals by their starting point
        #2) Compare previous interval's end with current one's start
        #3) In case of no overlap, move the previous end to the current interval's
        #4) In case of an overlap, use whichever end is smaller as the new previous end
        
        intervals.sort(key = lambda x: x[0]) #Sort by starting point
        
        output, previousEnd = 0, intervals[0][1]
        for start, end in intervals[1:]:
            #No overlap
            if previousEnd <= start:
                previousEnd = end
            #Overlap
            else:
                previousEnd = min(previousEnd, end)
                output += 1
        
        return output