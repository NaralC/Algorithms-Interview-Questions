class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        # Time: O(mn)
        # Space: O(1)
        
        ROWS, COLS = len(matrix), len(matrix[0])
        
        # Flag a cell by flipping its top most col and left most row to 0
        # How do we flag the top most row and the left most col? Use extra variables
        setZeroFirstRow = setZeroFirstCol = False
        
        for row in range(ROWS):
            for col in range(COLS):
                if not matrix[row][col]:
                    if not row:
                        setZeroFirstRow = True
                    if not col:
                        setZeroFirstCol = True
                        
                    matrix[row][0] = matrix[0][col] = 0
        
        
        # Update cells according to their flags but skip the first row and col
        for row in range(1, ROWS):
            for col in range(1, COLS):
                if not matrix[row][0] or not matrix[0][col]:
                    matrix[row][col] = 0
                    
        # Clean up the top most row and the left most col
        if setZeroFirstRow:
            for col in range(COLS):
                matrix[0][col] = 0
        
        if setZeroFirstCol:
            for row in range(ROWS):
                matrix[row][0] = 0