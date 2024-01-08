class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # Time: O(nlogn)
        # Space: O(n)

        count = 0
        stack = []

        for cur in sorted(intervals, key = lambda x: x[0]):
            if not len(stack):
                stack.append(cur)
                continue

            # Overlap, be greedy. Keep whichever interval ending first
            if (top := stack[-1])[1] > cur[0]:
                stack[-1] = cur if cur[1] < top[1] else top
                count += 1

            # No Overlap
            else:
                stack.append(cur)
        
        return count
        