class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        # Time: O(n)
        # Space: O(n)
        
        overlap = []
        idx1, idx2 = 0, 0
        
        while idx1 < len(firstList) and idx2 < len(secondList):
            # Check for overlap
            start = max(firstList[idx1][0], secondList[idx2][0])
            end = min(firstList[idx1][1], secondList[idx2][1])
            
            if start <= end:
                overlap.append((start, end))
            
            # Move on from the interval with smaller ending
            if firstList[idx1][1] < secondList[idx2][1]:
                idx1 += 1
            else:
                idx2 += 1
        
        return overlap