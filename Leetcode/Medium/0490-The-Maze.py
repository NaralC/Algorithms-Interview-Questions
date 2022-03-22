class Solution:
    def hasPath(self, maze, start, destination):
        #Time: O(mn)
        #Space: O(mn)
        m, n, stopped = len(maze), len(maze[0]), set()
        
        def dfs(x, y):
            #Prevent loop
            if (x, y) in stopped: 
                return False
            stopped.add((x, y))
            
            if [x, y] == destination:
                return True
            
            #Continue DFS in each direction
            for i, j in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                newX, newY = x, y
                
                while 0 <= newX + i < m and 0 <= newY + j < n and maze[newX + i][newY + j] != 1:
                    newX += i
                    newY += j
                    
                if dfs(newX, newY):
                    return True
                
            return False
        return dfs(*start)