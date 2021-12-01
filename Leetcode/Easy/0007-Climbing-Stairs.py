class Solution:
    def climbStairs(self, n: int) -> int:
        #Time: O(n)
        #Space: O(n)
        travel = [0] * (n + 1) #+1 since there's a ground level
        travel[0] = 1 #There's only one way to reach the ground: to not move at all
        
        for idx in range(1, len(travel)):
            previousOne = travel[idx - 1] if idx - 1 >= 0 else 0
            previousTwo = travel[idx - 2] if idx - 2 >= 0 else 0
            
            travel[idx] = previousOne + previousTwo
        
        return travel[-1]