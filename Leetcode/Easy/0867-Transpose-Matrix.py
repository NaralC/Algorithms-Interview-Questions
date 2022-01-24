class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        #Time: O(m*n)
        #Space: O(m*n)
        
        ROW, COL = len(matrix), len(matrix[0])
        newMatrix = [[None for _ in range(ROW)] for _ in range(COL)]
        
        #We swap when row != col
        for row in range(COL):
            for col in range(ROW):
                if row == col:
                    newMatrix[row][col] = matrix[row][col]
                else:
                    newMatrix[row][col] = matrix[col][row]
                    
        return newMatrix