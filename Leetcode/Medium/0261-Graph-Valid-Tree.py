from collections import defaultdict

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # Time: O(v + e)
        # Space: O(v + e)
        
        def dfs(node):
            # Prevent loop
            if node in seen:
                return
            seen.add(node)
            visited[node] = True
            
            # Continue DFS
            for nextNode in adj[node]:
                dfs(nextNode)
            
            seen.remove(node)
            adj[node] = []
        
        def reachGoal(node, goal):
            # Prevent loop
            if node in seen:
                return
            seen.add(node)
            
            if node == goal:
                return True
            
            # Continue DFS
            for nextNode in adj[node]:
                if reachGoal(nextNode, goal):
                    return True
            
            seen.remove(node)
        
        
        # Before connecting an edge, see if it's possible to travel from node1 to node2 of the edge
        adj = defaultdict(list)
        seen = set()
        
        for n1, n2 in edges:
            # If n2 can be reached from n1, then there's already a node providing the necessary path
            # Return false as the graph now has multiple ways to arrive at certain nodes - invalidating it as a tree
            if reachGoal(n1, n2):
                return False
            
            # Safe to connect edge
            adj[n1].append(n2)
            adj[n2].append(n1)
        
        # Run DFS again starting from one node to see if all nodes are connected
        visited = [False] * n
        dfs(0)
        
        return False not in visited