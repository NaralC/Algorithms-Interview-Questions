from collections import defaultdict

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        #Time: O(n^2)
        #Space: O(n)
        #Construct our graph edge by edge and return an edge whose nodes are reachable via other edges already
        
        def reachEnd(n1, n2):
            #Loop detected, path can't be reached with this edge
            if n1 in seen:
                return False
            seen.add(n1)
            
            #If n1 -> n2, then this edge is redundant cause a path is already paved
            if n1 == n2:
                return True
            
            #Continue DFS
            for neighbor in adj[n1]:
                if reachEnd(neighbor, n2):
                    return True
        
        adj = defaultdict(list)
        output = []
        
        for n1, n2 in edges:
            #Prevent loop
            seen = set()
            
            #If n1 -> n2 then there's already a path already made, so this edge is reduntant
            if reachEnd(n1, n2):
                output = [n1, n2]
            
            #Safe to connect the nodes
            adj[n1].append(n2)
            adj[n2].append(n1)
        
        return output