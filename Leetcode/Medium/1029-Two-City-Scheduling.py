class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        #Time: O(nlogn)
        #Space: O(1)
        #Greedily sort costs based on the gap between A and B, and pour the first half to A. The idea is "How much money can we save by sending this person to A instead of B"
        #The other way around works too
        
        costs = sorted(costs, key = lambda x: x[0] - x[1])
        output = 0
        
        for idx in range(len(costs) // 2):
            output += costs[idx][0] + costs[-1 - idx][1]
        
        return output
        
        