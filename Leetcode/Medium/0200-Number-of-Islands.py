class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        #Time: O(m * n)
        #Space: O(m * n)
    
        # Perform a DFS to loop through all lands
        # Should we run into a land, sink all adjacent lands by turning them into 0's and finally increment the total count
        # Return the total count
        
        output = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == '1':
                    output += 1
                    sinkIsland(row, col, grid)
        
        return output
    
def sinkIsland(row, col, grid):
    #Boundary check/Keep the sinking process inside the island
    if (row < 0 or row > len(grid) - 1) or (col < 0 or col > len(grid[0]) - 1) or grid[row][col] == '0':
        return
    
    grid[row][col] = '0' #sink the current land
    sinkIsland(row - 1, col, grid) #top
    sinkIsland(row + 1, col, grid) #bottom
    sinkIsland(row, col - 1, grid) #left
    sinkIsland(row, col + 1, grid) #right