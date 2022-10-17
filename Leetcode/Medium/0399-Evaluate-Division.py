from collections import defaultdict

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        # Time: O(n + mn)
        # Space: O(n)
        # where m = len(queries), n = len(equations)
        
        def dfs(cur, end, carry):
            # Prevent infinite recursion
            if cur in visited: return
            visited.add(cur)
            
            if cur == end:
                output.append(carry)
                return True
            
            for nxt in adj[cur]:
                if dfs(nxt, end, carry * adj[cur][nxt]):
                    return True

            return
        
        # Adjacency list depicting mathematical relationships between numbers
        adj = defaultdict(dict) # { numerator : { denom : numerator / denom, ... } }
        
        for e, v in zip(equations, values):
            num, denom = e
            adj[num][denom] = v
            adj[denom][num] = 1 / v
        
        # DFS through our adj
        output = []
        
        for num, denom in queries:
            if num not in adj:
                output.append(-1)
            
            elif num == denom:
                output.append(1)
            
            else:
                visited = set()
                if not dfs(num, denom, 1):
                    output.append(-1)
            
        return output
    