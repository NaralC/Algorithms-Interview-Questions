class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        # Time: O(nlogn)
        # Space: O(n)
        
        intervals = sorted(firstList + secondList)
        
        # Interval question
        overlap = []
        latestEnd = intervals[0][1]
        
        for i in intervals[1:]:
            # Overlap
            if latestEnd >= i[0]:
                overlap.append((i[0], min(i[1], latestEnd)))
                latestEnd = max(latestEnd, i[1])
            
            # No overlap
            else:
                latestEnd = i[1]
                
        return overlap