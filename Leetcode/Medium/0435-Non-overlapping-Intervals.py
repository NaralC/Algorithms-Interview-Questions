class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # Time: O(nlogn)
        # Space: O(n)
        
        intervals.sort()
        stack = []
        
        for cur in intervals:
            # Overlap: keep the interval that ends first
            if len(stack) and stack[-1][1] > cur[0]:
                if stack[-1][1] > cur[1]:
                    stack[-1] = cur
            
            # No overlap
            else:
                stack.append(cur)
            
        return len(intervals) - len(stack)