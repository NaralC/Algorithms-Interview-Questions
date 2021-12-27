class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        constantSpace(matrix)
        
def constantSpace(matrix):
    firstRowZero, firstColZero = False, False
    
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            if matrix[row][col] == 0:
                if row == 0: firstRowZero = True
                if col == 0: firstColZero = True
                
                matrix[0][col] = 0
                matrix[row][0] = 0
                
    for row in range(1, len(matrix)):
        for col in range(1, len(matrix[0])):
            if matrix[0][col] == 0 or matrix[row][0] == 0:
                matrix[row][col] = 0
                
    if firstRowZero:
        for col in range(1, len(matrix[0])):
            matrix[0][col] = 0
    
    if firstColZero:
        for row in range(1, len(matrix)):
            matrix[row][0] = 0
        
def extraSpace(matrix):
    #Time: O(m * n) looping through every elemen
    #Space: O(m + n) in the worst case where all rows and cols need to be set to zero

    rows, cols = set(), set()

    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            if matrix[row][col] == 0:
                rows.add(row)
                cols.add(col)

    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            if row in rows or col in cols:
                matrix[row][col] = 0