from collections import defaultdict

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        # Time: O(?)
        # Space: O(?)
        
        def arrive(current, end):
            # Prevent loop
            if current in seen:
                return
            seen.add(current)
            
            # Check if we've reached the goal
            if current == end:
                return True
            
            # Continue DFS
            for nextNode in adj[current]:
                if arrive(nextNode, end):
                    return True
            
            # Relax edge
            seen.remove(current)
        
        # Initialize our adjacency list
        adj = defaultdict(list)
            
        # Keep building our graph up edge by edge, return the one that causes redundancy
        seen = set()
        
        for n1, n2 in edges:
            # If we arrive at n2, that means there's already a path connected - rendering this current edge redundant
            if arrive(n1, n2):
                return [n1, n2]
            
            # Safe to connect edge
            adj[n1].append(n2)
            adj[n2].append(n1)
        
        return