class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        #Time: O(3^n)
        #Space: O(3^n)
        
        def dfs(row, col, visitedCells, output):
            #Prevent boundary break
            if row < 0 or col < 0 or row >= len(grid) or col >= len(grid[0]):
                return
            
            #Prevent walking over obstacles
            if grid[row][col] == -1:
                return
            
            #Terminate when we reach the end
            if grid[row][col] == 2:
                #Increment the count only iff we've walked over all empty cells
                if visitedCells == emptyCells:
                    output[0] += 1
                return
                    
            #Continue the traversal
            visitedCells += 1
            grid[row][col] = -1 #Mark this to prevent infinite recursions
            
            dfs(row + 1, col, visitedCells, output)
            dfs(row, col + 1, visitedCells, output)
            dfs(row - 1, col, visitedCells, output)
            dfs(row, col - 1, visitedCells, output)
            
            grid[row][col] = 0 #Unmark this to let other DFSs traverse over it
        
        #Get the starting coordinates and the number of empty cells
        x, y = None, None
        emptyCells = 1
        
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    x, y = row, col
                
                elif grid[row][col] == 0:
                    emptyCells += 1
        
        #Use DFS - if we reach the end and have traversed over all empty cells -> increment count
        output = [0]
        dfs(x, y, 0, output)
        return output[0]