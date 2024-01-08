class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # Time: O(nlogn)
        # Space: O(n)

        stack = []

        for cur in sorted(intervals, key = lambda x: x[0]):
            if not len(stack):
                stack.append(cur)
                continue

            # Overlap
            if (top := stack[-1])[1] >= cur[0]:
                stack[-1] = [min(top[0], cur[0]), max(top[1], cur[1])]

            # No Overlap
            else:
                stack.append(cur)

        return stack
