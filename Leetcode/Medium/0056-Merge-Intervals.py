class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        #Time: O(n log(n))
        #Space: O(n)
        intervals.sort(key = lambda x: x[0]) #Sort everything by their starting point
        output = [intervals[0]]
        
        for current in intervals[1:]:
            latest = output[-1]
            
            #In case of an overlap with the latest interval
            if latest[1] >= current[0]:
                latest[1] = max(latest[1], current[1])
            #No overlap with the latest interval
            else:
                output.append(current)
                    
        return output