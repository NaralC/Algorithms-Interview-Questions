from collections import defaultdict

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Time: O(v + e)
        # Space: O(v + e)
        
        def dfs(course):
            if course in cycle:
                return False
            
            # Continue DFS
            cycle.add(course)
            for pre in adj[course]:
                if not dfs(pre):
                    return False
            
            # Prevent repetitive work
            adj[course] = []
            cycle.remove(course)
            return True
        
        # Form an adjacency list
        adj = defaultdict(list)
        
        for course, pre in prerequisites:
            adj[course].append(pre)
            
        # DFS starting from every courses
        cycle = set()
        
        for course in range(numCourses):
            if not dfs(course):
                return False
            
        return True