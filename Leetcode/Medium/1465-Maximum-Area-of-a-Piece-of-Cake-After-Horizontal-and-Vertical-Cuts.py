class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        # Time: O(nlogn + mlogm)
        # Space: O(1)
        
        # Sort the arrs, compute max diff between 2 consecutive elements in each arrs
        # This will give us max width and max height -> multiply them
        horizontalCuts.sort()
        verticalCuts.sort()
        
        # Deal with cases with only a single cut to either/both dimensions
        # By considering the edges first
        max_width = max(verticalCuts[0], w - verticalCuts[-1])
        max_height = max(horizontalCuts[0], h - horizontalCuts[-1])
        
        for idx in range(len(verticalCuts) - 1):
            max_width = max(max_width, verticalCuts[idx + 1] - verticalCuts[idx])
            
        for idx in range(len(horizontalCuts) - 1):
            max_height = max(max_height, horizontalCuts[idx + 1] - horizontalCuts[idx])

        return (max_width * max_height) % (pow(10, 9) + 7)
        