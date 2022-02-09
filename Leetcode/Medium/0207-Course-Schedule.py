class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        #Time: O(v + e)
        #Space: O(v)
        
        def dfs(course):
            #Base case: loop detected
            if course in seen:
                return False
            
            #Mark current node as visited
            visited[course] = True
            seen.add(course)
            
            #Continue the traversal
            for next_course in req[course]:
                if not dfs(next_course):
                    return False
            
            seen.remove(course) #Let other recursive calls traverse through the current node
            req[course] = [] #Path exhausted, prevent repeated work
            
            return True
        
        #Set up variables
        visited = [False for _ in range(numCourses)]
        req = {course : [] for course in range(numCourses)}
        seen = set()
        
        #Map which courses point to which into our dict
        for pair in prerequisites:
            next_course, course = pair
            req[course] += [next_course]
        
        #Start graph traversal with DFS
        for course in range(numCourses):
            if not dfs(course): #Terminate if a loop is detected
                return False
            
        return False not in visited #Return whether all nodes have been visited