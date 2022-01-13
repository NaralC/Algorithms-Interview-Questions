class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        #Time: O(nlogn)
        #Space: O(1)
        #The idea is the same is 'Non-overlapping Intervals' but a few modifications
        
        points.sort(key = lambda x: x[1])
        
        prevEnd = points[0][1]
        count = 1
        
        for currentStart, currentEnd in points:
            #Overlap - group as many balloons by their ending point, so we can shoot them all down later
            if prevEnd >= currentStart:
                prevEnd = min(prevEnd, currentEnd)
            
            #No overlap - time to shoot down the previous set of balloons
            else:
                count += 1
                prevEnd = currentEnd
        
        return count