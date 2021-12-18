class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        #Time: O(n)
        #Space: O(n)
        output = []
        
        for idx, current in enumerate(intervals):
            #Edge case: the new interval goes before the current one
            if newInterval[1] < current[0]:
                output.append(newInterval)
                return output + intervals[idx:]
            
            #The new interval goes after the current one
            elif newInterval[0] > current[1]:
                output.append(current)
            
            #The new intervals overlaps with the current one
            else:
                newInterval = [min(newInterval[0], current[0]),
                               max(newInterval[1], current[1])]
        
        output.append(newInterval)
        return output