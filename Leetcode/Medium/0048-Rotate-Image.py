class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        #Time: O(n^2) since we need to rotate every cell
        #Space: O(1)
        
        """
        Do not return anything, modify matrix in-place instead.
        """
        left, right = 0, len(matrix) - 1
        
        while left < right:
            for idx in range(right - left):
                top, bot = left, right
                
                #Save top left
                topLeft = matrix[top][left + idx]
                
                #Move bot left into top left
                matrix[top][left + idx] = matrix[bot - idx][left]
                
                #Move bot right into bot left
                matrix[bot - idx][left] = matrix[bot][right - idx]
                
                #Move top right into bot right
                matrix[bot][right - idx] = matrix[top + idx][right]
                
                #Move top left into top right
                matrix[top + idx][right] = topLeft
                
            left += 1
            right -= 1