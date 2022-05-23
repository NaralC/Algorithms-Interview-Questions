class Solution:
    def numWays(self, n: int, k: int) -> int:
        # Time: O(n)
        # Space: O(n)
        
        if n == 1:
            return k
        if n == 2:
            return k * k
        
        # Two choices at each idx, either paint the same or different color compared the previous fence
        # Make it same: color(idx - 1) * 1 if color(idx - 2) != color(idx - 1)
        # Make it different: color(idx - 1) * (k - 1)
        
        dp = [None] * (n + 1)
        dp[0] = 0
        dp[1] = k # One post, k ways to paint
        dp[2] = k * k # Two posts, k^2 ways to paint since we're allowed to paint at most 2 same colors
        
        # Add up the two choices mentioned above
        for idx in range(3, n + 1):
            dp[idx] = dp[idx - 1] * (k - 1) + dp[idx - 2] * (k - 1)
        
        return dp[-1]