class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:        
        #Time: O(v + e)
        #Space: O(v + e)
        
        def dfs(node):
            #Prevent repeated work
            if visited[node]:
                return
            visited[node] = True
            
            #Continue DFS
            neighbors = isConnected[node]
            
            for nextNode in range(len(neighbors)):
                status = neighbors[nextNode]
                if status == 1:
                    dfs(nextNode)
                
            #Prevent repeated work
            isConnected[node] = []
        
        #Use an array to track visited nodes
        nodes = len(isConnected[0])
        visited = [False for _ in range(nodes)]
        
        #DFS on every node
        count = 0
        
        for start in range(nodes):
            if not visited[start]:
                dfs(start)
                count += 1
        
        return count