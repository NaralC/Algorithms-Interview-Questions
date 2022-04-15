class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # Time: O(n)
        # Space: O(n)
        
        if len(cost) < 3:
            return min(cost)
        
        # Account for the last step (the goal) where it has no cost
        lookup = [float('inf')] * (len(cost) + 1)
        lookup[-1] = 0
        
        # Start by iterating from the back
        for idx in reversed(range(len(lookup) - 1)):
            
            # Iterate forward by 2 positions, take the minimum cost for connecting steps            
            if idx < len(lookup) - 1:
                lookup[idx] = min(lookup[idx], cost[idx] + lookup[idx + 1])

            if idx < len(lookup) - 2:
                lookup[idx] = min(lookup[idx], cost[idx] + lookup[idx + 2])
        
        return min(lookup[:2])