from collections import defaultdict

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # Time: O(v + e)
        # Space: O(v + e)
        
        def dfs(course):
            if course in completed:
                return True
            
            if course in current_cycle:
                return False
            
            current_cycle.add(course)
            for pre in adj[course]:
                if not dfs(pre):
                    return False
            
            completed.add(course)
            order.append(course)
            current_cycle.remove(course)
            return True
        
        # Form an adjacency list
        adj = defaultdict(list)
        
        for course, pre in prerequisites:
            adj[course].append(pre)
        
        # DFS, starting from every courses
        order = []
        completed = set() # check whether element in order or not
        current_cycle = set() # check for self-loops
        
        for course in range(numCourses):
            if not dfs(course):
                return []
        
        return order