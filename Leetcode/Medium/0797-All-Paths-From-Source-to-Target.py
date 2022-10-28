class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        # Time: O(2^n * n)
        # Space: O(n)
        
        def dfs(node, path):
            # No need to prevent infinite recursion as the graph's acyclic
            path.append(node)
            
            # Reached the end
            if node == len(graph) - 1:
                output.append(path)
                return
            
            # Continue DFS
            for nxt in graph[node]:
                dfs(nxt, path.copy())
            
            return
        
        output = []
        dfs(0, [])
        return output
    