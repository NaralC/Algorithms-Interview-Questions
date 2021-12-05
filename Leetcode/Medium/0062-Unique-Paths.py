class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        #Time: O(n * m)
        #Space: O(n * m)
        memoize = [[0 for _ in range(n)] for _ in range(m)]
        
        for row in range(m):
            for col in range(n):
                #Only 1 way to reach the top row: strictly going right
                if row == 0:
                    memoize[row][col] = 1
                    
                #Only 1 way to reach the left most column: strictly going down
                elif col == 0:
                    memoize[row][col] = 1
                    
                else:
                #Ways to reach current spot = ways to reach its left + ways to reach its top
                    waysToReachLeft = memoize[row][col - 1] 
                    waysToReachTop = memoize[row - 1][col]
                    memoize[row][col] = waysToReachLeft + waysToReachTop
        
        #Return the ways to reach the bottom right spot
        return memoize[-1][-1]
                