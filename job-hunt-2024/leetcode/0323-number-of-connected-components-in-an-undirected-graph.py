class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # Time: O(n + e)
        # Space: O(n + e)

        def dfs(node):
            # Prevent cycle
            if node in seen: return
            seen.add(node)

            # Continue
            for nxt in adj[node]:
                dfs(nxt)

            # Prevent repitition
            adj[node] = []
            return

        # Form an adjacency list
        adj = defaultdict(list)

        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)

        # Count how many pieces there are
        seen = set()
        count = 0

        for start in range(n):
            if start not in seen:
                dfs(start)
                count += 1

        return count
