class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        #Time: O(m*n)
        #Space: O(m*n)
        
        ROW, COL = len(heights), len(heights[0])
        reach_pac, reach_at = set(), set()
        
        #Iterate starting from top and bottom rows
        for col in range(COL):
            canFlow(heights, 0, col, heights[0][col], reach_pac) #Pacific adjacent
            canFlow(heights, ROW - 1, col, heights[ROW - 1][col], reach_at) #Atlantic adjacent
            
        #Iterate starting from left and rightmost columns
        for row in range(ROW):
            canFlow(heights, row, 0, heights[row][0], reach_pac) #Pacific adjacent
            canFlow(heights, row, COL - 1, heights[row][COL - 1], reach_at) #Atlantic adjacent
        
        #Return cells where water from both oceans can reach
        return list(reach_pac.intersection(reach_at))
    
def canFlow(heights, row, col, prevHeight, visited):
    #Prevent boundary break
    if row < 0 or col < 0 or row >= len(heights) or col >= len(heights[row]):
        return
    
    #Since we're doing this in reverse, water must flow from low -> hi ground
    #Also prevent repeated work
    if prevHeight > heights[row][col] or (row, col) in visited:
        return
    
    #Mark current cell as water-flow-friendly
    visited.add((row, col))
    
    #Try the same with the neighbors
    canFlow(heights, row - 1, col, heights[row][col], visited)
    canFlow(heights, row + 1, col, heights[row][col], visited)
    canFlow(heights, row, col - 1, heights[row][col], visited)
    canFlow(heights, row, col + 1, heights[row][col], visited)