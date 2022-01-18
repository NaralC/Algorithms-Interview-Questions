class Solution:
    def climbStairs(self, n: int) -> int:
        #Time: O(n)
        #Space: O(n)
        
        steps = [None for _ in range(n + 1)] #Account for step 0
        steps[0] = 1 #The only way to reach step 0 is to not move
        
        for idx in range(1, n + 1):
            #To get the number of ways to reach the current step, add up:
            #The number of ways n steps before that
            
            oneStepBefore = steps[idx - 1] if idx >= 1 else 0
            twoStepBefore = steps[idx - 2] if idx >= 2 else 0
            steps[idx] = oneStepBefore + twoStepBefore
        
        return steps[-1]