class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        #Time: O(m * n)
        #Space: O(m * n)

        #Check if the start or finish is blocked
        if obstacleGrid[0][0] == 1 or obstacleGrid[-1][-1] == 1:
            return 0
        
        ROWS, COLS = len(obstacleGrid), len(obstacleGrid[0])
        ways = [[0 for _ in range(COLS)] for _ in range(ROWS)]
        ways[0][0] = 1
        
        for row in range(ROWS):
            for col in range(COLS):
                if obstacleGrid[row][col] == 0:
                    #Skip this as it's already been processed
                    if row == 0 and col == 0: 
                        continue 
                    #Only works if we're not on left col
                    left = ways[row][col - 1] if col > 0 else 0 
                    #Only works if we're not on top row
                    top = ways[row - 1][col] if row > 0 else 0 
                    
                    ways[row][col] = left + top
                    
        return ways[-1][-1]