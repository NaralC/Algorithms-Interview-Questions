class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        return bottomUpTopology(n, edges)

def withoutIncomingEdges(n, edges):
    #Time: O(e) as we iterate all edges
    #Space: O(v) as we store vectices with no edges
    
    #Track whether each node has any incoming edges
    incoming = [False for _ in range(n)]
    
    #Mark down which nodes has incoming edges
    for outEdge, inEdge in edges:
        incoming[inEdge] = True
    
    #Only return nodes with no incoming edges
    return [idx for idx in range(len(incoming)) if not incoming[idx]]
        
def bottomUpTopology(n, edges):
    #Time: O(v + e) 
    #Space: O(v + e)

    def dfs(node):
        #Prevent repeated work
        if visited[node]:
            return
        visited[node] = True

        #See if we've reached the end
        if adj[node] == []:
            output.append(node)

        #Continue DFS
        for parent in adj[node]:
            dfs(parent)

    #Form an adjacency list (child -> parent topology)
    adj = collections.defaultdict(list)

    for parent, child in edges:
        adj[child].append(parent)

    #Bottom-up DFS on every node
    visited = [False for _ in range(n)]
    output = []

    for start in range(n):
        dfs(start)

    return output

