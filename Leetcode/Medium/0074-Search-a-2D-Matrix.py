class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # Time: O(m + n)
        # Space: O(1)
        
        # Start from bottom left
        row, col = len(matrix) - 1, 0
        
        while row > -1 and col < len(matrix[0]):
            # Target's bigger than current number
            if target > matrix[row][col]:
                col += 1
            
            # Target's smaller than current number
            elif target < matrix[row][col]:
                row -= 1
            
            # Found the target
            else:
                return True
        
        # In case the target doesn't exist in the matrix
        return False