class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # Time: O(n)
        # Space: O(n)
        
        left, right = [], []
        
        for cur in intervals:
            # The current interval goes before the new one
            if cur[1] < newInterval[0]:
                left.append(cur)
            
            # The current interval goes after the new one
            elif cur[0] > newInterval[1]:
                right.append(cur)
            
            # The current interval overlaps with the new one
            else:
                newInterval = [min(cur[0], newInterval[0]), max(cur[1], newInterval[1])]
        
        return left + [newInterval] + right