class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        from collections import defaultdict

        #Time: O(v + e)
        #Space: O(v + e)
        
        def dfs(node):
            #Prevent loop
            if visited[node]:
                return
            visited[node] = True
            
            for nextNode in neighbor[node]:
                dfs(nextNode)
            
            #Prevent repeated work
            neighbor[node] = []
        
        #Keep track of which nodes have been visited and form an adjacency list
        visited = [False for _ in range(n)]
        neighbor = defaultdict(list)
        
        for start, end in edges:
            neighbor[start].append(end)
            neighbor[end].append(start)
        
        #DFS every single node
        count = 0
        
        for start in range(n):
            if not visited[start]:
                dfs(start)
                count += 1
        
        return count