from collections import defaultdict

class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        #Time: O(n)
        #Space: O(n)
        
        def dfs(node):
            nonlocal count
            
            for neighbor in adj[node]:
                if neighbor in seen:
                    continue
                    
                #Check if this city can reach 0
                if (neighbor, node) not in edges:
                    count += 1
                
                seen.add(neighbor)
                dfs(neighbor)
        
        #Form a non-directional adj list and a set that tracks actual edges
        adj = defaultdict(list)
        edges = set()
        
        for n1, n2 in connections:
            adj[n1].append(n2)
            adj[n2].append(n1)
            
            edges.add((n1, n2))
        
        #DFS starting from 0, increment count when a node doesn't point towards 0
        count = 0
        seen = {0}
        
        dfs(0)
        return count