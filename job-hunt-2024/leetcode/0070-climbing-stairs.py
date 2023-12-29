class Solution:
    def climbStairs(self, n: int) -> int:
        # Time: O(n)
        # Space: O(n)
        
        # At each step, record the number of possible steps
        steps = [0 for _ in range(n + 1)]
        steps[0] = 1 # Only one way to be at start

        for idx in range(1, len(steps)):
            backOne = steps[idx - 1]
            backTwo = steps[idx - 2]
            steps[idx] = backOne + backTwo

        return steps[-1]
        