class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        #Time: O(height * width)
        #Space: O(1)
        height, width = len(grid), len(grid[0])
        
        #Elements in top most row can be accessed by only moving right
        for row in range(1, height):
            grid[row][0] += grid[row - 1][0]
        
        #Elements in top most row can be accessed by only moving down
        for col in range(1, width):
            grid[0][col] += grid[0][col - 1]
        
        #Same with Unique Paths, but we pick the minimum value instead of adding up both values
        for row in range(1, height):
            for col in range(1, width):
                grid[row][col] += min(grid[row - 1][col], grid[row][col - 1])
        
        return grid[-1][-1]