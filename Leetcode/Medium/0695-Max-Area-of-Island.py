from collections import deque

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # Time: O(mn)
        # Space: O(mn)
        # Loop through every cell -> Run into an island -> Sink it and update output
        
        def getSizeBFS(a, b):
            q = deque([(a, b)])
            area = 0
            
            while len(q):
                row, col = q.popleft()
                
                # Sink current cell if it's a 1
                if grid[row][col]:
                    grid[row][col] = 0
                    area += 1
                
                    # Append its neighbors to the q
                    if row > 0: q.append((row - 1, col)) #Top
                    
                    if row < len(grid) - 1: q.append((row + 1, col)) # Right
                        
                    if col > 0: q.append((row, col - 1)) # Left
                        
                    if col < len(grid[0]) - 1: q.append((row, col + 1)) # Bot
                    
            return area
        
        def getSizeDFS(row, col):
            # Prevent boundary break and only count 1's
            if row < 0 or col < 0 or row >= len(grid) or col >= len(grid[0]) or not grid[row][col]:
                return 0
            
            # Sink current cell
            grid[row][col] = 0
            
            # Continue sinking its neighbors
            top = getSizeDFS(row + 1, col)
            left = getSizeDFS(row - 1, col)
            right = getSizeDFS(row, col + 1)
            bot = getSizeDFS(row, col - 1)
            
            # Return the size of the island
            return 1 + top + left + right + bot            
        
        maxArea = 0
        
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col]:
                    maxArea = max(maxArea, getSizeBFS(row, col))
                    # maxArea = max(maxArea, getSizeDFS(row, col))
                    
        return maxArea