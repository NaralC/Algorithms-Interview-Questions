class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        #Time: O(m * n) with simultaneous BFS, no cells are visited twice
        #Space: O(m * n)
        
        #Checks whether this neighboring cell is in the matrix and isn't a wall
        def getNeighbor(row, col):
            #Prevent boundary break
            if row < 0 or col < 0 or row >= len(rooms) or col >= len(rooms[0]):
                return
            
            #Prevent repeated work and running into walls
            if visited[row][col] or rooms[row][col] == -1:
                return
            
            visited[row][col] = True
            queue.append([row, col])
        
        #Firstly, get the starting points, mark them as visited and add them to our queue
        visited = [[False for _ in range(len(rooms[0]))] for _ in range(len(rooms))]
        queue = deque()
        
        for row in range(len(rooms)):
            for col in range(len(rooms[0])):
                if not rooms[row][col]:
                    visited[row][col] = True
                    queue.append([row, col])
                    
        #Starting simultaneously spreading the distance with BFS
        distance = 0
        
        while queue:
            #For each loops don't work since they don't allow mutation during iteration
            #But for loops are taken a snapshot of instead
            for idx in range(len(queue)):
                row, col = queue.popleft()
                rooms[row][col] = distance
                
                #Get all of its adjacent cells
                getNeighbor(row - 1, col)
                getNeighbor(row, col - 1)
                getNeighbor(row + 1, col)
                getNeighbor(row, col + 1)
            
            distance += 1