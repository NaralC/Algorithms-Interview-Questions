class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Time: O(n + e)
        # Space: O(n + e)

        def cycleExists(cur):
            # Prevent cycle
            if cur in seen: return True
            seen.add(cur)

            # Continue
            for n in adj[cur]:
                if cycleExists(n): return True

            # Relax
            adj[cur] = [] # Prevents TLE
            seen.remove(cur)
            return False

        # Form an adjacency list
        adj = defaultdict(list) # { node: [...neighbors] }

        for a, b in prerequisites:
            adj[b].append(a)

        # Detect if there's a cycle
        seen = set()

        for n in range(numCourses):
            if cycleExists(n): return False

        return True
