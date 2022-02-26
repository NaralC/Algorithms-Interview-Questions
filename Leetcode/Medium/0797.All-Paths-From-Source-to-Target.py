class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        #Time: O(v + e)
        #Space: O(v + e)
        
        def dfs(current, history):
            #No need to check for loops as the input is an acyclic graph
            history.append(current)
            
            #Check if we've reached the end
            if current == len(graph) - 1:
                output.append(history)
            
            for nextNode in graph[current]:
                dfs(nextNode, history.copy())
        
        
        #Start graph traversal with DFS
        output = []
        
        dfs(0, [])
        
        return output