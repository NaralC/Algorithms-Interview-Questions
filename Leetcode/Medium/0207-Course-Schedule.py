class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Time: O(v + e)
        # Space: O(v + e)
        
        def dfs(node):
            # Prevent loop
            if node in seen:
                return False
            seen.add(node)
            
            # Continue DFS
            for nextNode in adj[node]:
                if not dfs(nextNode):
                    return False
                
            # Prevent repetitive work
            adj[node] = []
            seen.remove(node)
            
            return True
        
        # Form an adjacency list
        adj = defaultdict(list)
        
        for end, start in prerequisites:
            adj[start].append(end)
            
        # DFS starting from all possible nodes. If there's a loop -> impossible to complete all courses
        seen = set()
        
        for start in range(numCourses):
            if not dfs(start):
                return False
        
        return True