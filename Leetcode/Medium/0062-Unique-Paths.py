class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # Time: O(mn)
        # Space: O(mn)
        
        dp = [[0 for _ in range(n)] for _ in range(m)]
        
        for row in range(m):
            for col in range(n):
                # The top most row and leftmost col only have 1 way to reach since the robot can only go down or right
                if row == 0 or col == 0:
                    dp[row][col] = 1
                
                # Other cells can add up ways from its their left and their top
                else:
                    dp[row][col] = dp[row - 1][col] + dp[row][col - 1]
        
        return dp[-1][-1]