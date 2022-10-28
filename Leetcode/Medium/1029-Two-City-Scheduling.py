class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        # Time: O(nlogn)
        # Space: O(1)
        
        # Greedy - sort by difference in price
        costs.sort(key = lambda x: x[0] - x[1])
        total = 0
        l = 0
        r = len(costs) - 1
        
        while l <= r:
            total += costs[l][0] + costs[r][1]
            l += 1; r -= 1
        
        return total
        