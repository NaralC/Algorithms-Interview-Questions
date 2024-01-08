class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # Time: O(n)
        # Space: O(n)

        before, after = [], []

        for cur in intervals:
            # Current interval goes before new interval
            if cur[1] < newInterval[0]:
                before.append(cur)

            # Current interval goes after new interval
            elif newInterval[1] < cur[0]:
                after.append(cur)

            # Overlap, merge current into new
            else:
                newInterval = [min(cur[0], newInterval[0]), max(cur[1], newInterval[1])]

        return before + [newInterval] + after
        