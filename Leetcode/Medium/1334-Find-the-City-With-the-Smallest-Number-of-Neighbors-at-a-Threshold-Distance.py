class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        # Time: O(v^3) follows Floyd-Warshall doc
        # Space: O(v)
        # where v = number of vertices
        
        # Form an adjacency to track shortest path between all pairs
        adj = { node : [float('inf')] * n for node in range(n) }
        
        for start, end, weight in edges:
            adj[start][start] = adj[end][end] = 0
            adj[start][end] = adj[end][start] = weight
            
        # Deploy Floyd-Warshall to find shortest path between all pairs
        for between in range(n):
            for start in range(n):
                for end in range(n):
                    # Compare with intermediate distance through another node
                    #    c
                    #  /   \
                    # a --- b
                    
                    adj[start][end] = min(adj[start][end], adj[start][between] + adj[between][end])
        
        # Ship output
        city = float('-inf') # city number
        min_neigh = float('inf') # minimum neighbor count
        
        for start in range(n):
            count = 0 # number of neighbors
            
            for nxt in range(n):
                # Prevent self-loop / unreachable cities
                if start == nxt or adj[nxt][start] == float('inf'):
                    continue
                
                if adj[start][nxt] <= distanceThreshold:
                    count += 1
                
            if count <= min_neigh:
                min_neigh = count
                city = max(city, start)
        
        return city
        