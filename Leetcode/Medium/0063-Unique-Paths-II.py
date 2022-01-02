class Solution:
    def uniquePathsWithObstacles(self, grid: List[List[int]]) -> int:
        #Time: O(m * n)
        #Space: O(m * n)
        
        #Return 0 if either the start or finish is blocked
        if grid[0][0] or grid[-1][-1]:
            return 0
        
        ROWS, COLS = len(grid), len(grid[0])
        dp = [[0 for _ in range(COLS)] for _ in range(ROWS)]
        dp[0][0] = 1
        
        #First row
        for col in range(1, COLS):
            dp[0][col] = dp[0][col - 1] if grid[0][col] == 0 else 0
        
        #First col
        for row in range(1, ROWS):
            dp[row][0] = dp[row - 1][0] if grid[row][0] == 0 else 0
        
        #Remaining cells
        for row in range(1, ROWS):
            for col in range(1, COLS):
                if grid[row][col] == 0:
                    dp[row][col] = dp[row - 1][col] + dp[row][col - 1]
        
        return dp[-1][-1]       