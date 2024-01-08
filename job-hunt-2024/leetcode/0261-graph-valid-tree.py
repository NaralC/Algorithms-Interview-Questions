class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # Time: O(n + e)
        # Space: O(n + e)

        def hasCycle(cur, prev = -1):
            # Detect cycle
            if seen[cur]: return True
            seen[cur] = True

            # Continue
            for nxt in adj[cur]:
                # Prevent revisiting a previous node due to the graph being undirected
                if prev == nxt: continue
                if hasCycle(nxt, cur): return True

            # Prevent repitition
            adj[cur] = []
            return False

        # Form an adjacency list
        seen = [False] * n
        adj = defaultdict(list)

        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)

        # Check if all nodes are visited in one go with no cycles
        if hasCycle(0): return False
        
        for visited in seen:
            if not visited: return False
        return True
        