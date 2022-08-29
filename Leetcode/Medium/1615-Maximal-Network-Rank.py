from collections import defaultdict

class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        # Time: O(n^2)
        # Space: O(e)
        
        # Form an adjacency list
        adj = defaultdict(list)
        
        for cityA, cityB in roads:
            adj[cityA].append(cityB)
            adj[cityB].append(cityA)
            
        # Count the number of edges directly connected to both nodes, while subtracting redundant ones
        output = 0
        
        for cityA in range(n):
            for cityB in range(cityA + 1, n):
                redundantEdge = 1 if cityA in adj[cityB] else 0 # Big brain move
                
                output = max(output, len(adj[cityA]) + len(adj[cityB]) - redundantEdge)
        
        return output