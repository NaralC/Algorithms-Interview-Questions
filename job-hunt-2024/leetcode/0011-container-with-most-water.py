class Solution:
    def maxArea(self, height: List[int]) -> int:
        # Time: O(n)
        # Space: O(1)

        # Greedy?
        l, r = 0, len(height) - 1
        maxWater = 0

        while l < r:
            size = min(height[l], height[r]) * abs(l - r)
            maxWater = max(maxWater, size)

            if height[l] > height[r]:
                r -= 1
            else:
                l += 1
        
        return maxWater

        
