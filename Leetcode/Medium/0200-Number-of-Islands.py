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
                    sinkNeighbors(row, col, grid)
                    output += 1
        
        return output
    
def sinkNeighbors(row, col, grid):
    if (row < 0 or row >= len(grid)) or (col < 0 or col >= len(grid[0])): return #Boundary check
    if grid[row][col] == '0': return #Keep the sinking process from spreading out of the island
    
    grid[row][col] = '0'
    
    sinkNeighbors(row - 1, col, grid) #Top
    sinkNeighbors(row + 1, col, grid) #Bottom
    sinkNeighbors(row, col - 1, grid) #Left
    sinkNeighbors(row, col + 1, grid) #Right