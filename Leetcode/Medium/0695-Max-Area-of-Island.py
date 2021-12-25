class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        #Time: O(m * n)
        #Space: O(m * n) where the worst case is the whole grid being one island
        
        output = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    output = max(output, getSizeAndSink(row, col, grid))
        
        return output
    
def getSizeAndSink(row, col, grid):
    #Boundary check/Keeping the sinking process inside the island
    if (row < 0 or row > len(grid) - 1) or (col < 0 or col > len(grid[0]) - 1) or grid[row][col] == 0:
        return 0
    
    grid[row][col] = 0 #sink the current land
    top = getSizeAndSink(row - 1, col, grid)
    bot = getSizeAndSink(row + 1, col, grid)
    left = getSizeAndSink(row, col - 1, grid)
    right = getSizeAndSink(row, col + 1, grid)
    
    return 1 + top + bot + left + right