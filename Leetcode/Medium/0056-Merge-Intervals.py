class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # Time: O(nlogn)
        # Space: O(n)
        
        stack = []
        
        for start, end in sorted(intervals):
            # Overlap
            if len(stack) and stack[-1][1] >= start:
                stack[-1][1] = max(stack[-1][1], end)
            
            # No overlap
            else:
                stack.append([start, end])
        
        return stack