class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        #Time: O(n)
        #Space: O(n)
        output = []
        
        for idx, current in enumerate(intervals):
            #The new one goes before the current
            if newInterval[1] < current[0]:
                output.append(newInterval)
                return output + intervals[idx:]
            
            #The new one goes after the current (could be after any intervals)
            elif newInterval[0] > current[1]:
                output.append(current)
            
            #Overlap
            else:
                newInterval = [min(current[0], newInterval[0]),
                               max(current[1], newInterval[1])]
        
        output.append(newInterval)
        return output