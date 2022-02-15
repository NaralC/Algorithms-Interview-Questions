class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        #Time: O(m * n)
        #Space: O(1)
        
        def count(row, col):
            #Count which sides aren't connected to another land
            output = 0
            
            #Top border, increment when we're on the topmost row or there's no land above
            if row == 0 or not grid[row - 1][col]:
                output += 1
            
            #Bottom border, increment when we're on the bottommost row or there's no land below
            if row == len(grid) - 1 or not grid[row + 1][col]:
                output += 1
                
            #Left border, increment when we're on the leftmost column or there's no land to the left
            if col == 0 or not grid[row][col - 1]:
                output += 1
            
            #Right border, increment when we're on the rightmost column or there's no land to the right
            if col == len(grid[0]) - 1 or not grid[row][col + 1]:
                output += 1
            
            return output
        
        #Keep track of parameter
        perimeter = 0
        
        #Iterate over all cells
        for row in range(len(grid)):
            for col in range(len(grid[row])):
                if grid[row][col] == 1:
                    perimeter += count(row, col)
        
        return perimeter