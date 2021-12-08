class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        #val too high -> move left
        #val too low -> move down
        #Time: O(m * n)
        #Space: O(1)
        row, col = 0, len(matrix[0]) - 1
        
        while row < len(matrix) and col > -1:
            curVal = matrix[row][col]
            
            if curVal > target:
                col -= 1
            elif curVal < target:
                row += 1
            else:
                return True
        
        return False