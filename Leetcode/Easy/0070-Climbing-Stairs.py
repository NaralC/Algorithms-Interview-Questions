class Solution:
    def climbStairs(self, n: int) -> int:
        # Time: O(n)
        # Space: O(n)
        # Since it's either 1 or 2 at each step, take the sum of 2 previous steps as the current step's value
        
        # Account for the ground floor (which has 1 way of reaching it - not moving)
        ways = [0] * (n + 1)
        ways[0] = 1
        
        for idx in range(1, len(ways)):
            ways[idx] += ways[idx - 2] if idx > 0 else 0
            ways[idx] += ways[idx - 1] if idx > 0 else 0
                  
        return ways[-1]