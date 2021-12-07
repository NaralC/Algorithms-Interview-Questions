class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        #Time: O(n^2) since both the loops and output array are nested
        #Space: O(n^2)
        output = []
        
        for row in range(numRows):
            newRow = [None for _ in range(row + 1)]
            newRow[0], newRow[-1] = 1, 1
            
            for col in range(1, row):
                newRow[col] = output[row - 1][col - 1] + output[row - 1][col]
            
            output.append(newRow)
        
        return output