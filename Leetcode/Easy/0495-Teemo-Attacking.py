class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:    
        return optimized(timeSeries, duration)
    
def optimized(timeSeries, duration):
    #Time: O(n)
    #Space: O(n)
    
    #There's no reset after the last element - thus we're skipping it
    total = 0
    for idx in range(len(timeSeries) - 1):
        total += min(duration, timeSeries[idx + 1] - timeSeries[idx])
    
    return total + duration
        
def mergeIntervals(timeSeries, duration):
    #Time: O(n)
    #Space: O(n)

    #get the percise time intervals
    intervals = []
    for time in timeSeries:
        intervals.append([time, time + duration - 1])

    #now we merge the intervals together
    stack = [intervals[0]]
    for start, end in intervals[1:]:
        #overlap
        if stack[-1][1] >= start:
            stack[-1][1] = max(stack[-1][-1], end)
        #no overlap
        else:
            stack.append([start, end])

    #count the number of seconds Ashe is poisoned
    count = 0
    for start, end in stack:
        count += end - start + 1

    return count