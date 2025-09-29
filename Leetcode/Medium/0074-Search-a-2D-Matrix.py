# Staircase version
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # Time: O(log(mn))
        # Space: O(1)

        # If target not in matrix
        if target < matrix[0][0] and target > matrix[-1][-1]: return False

        # Start from bottom left
        row, col = len(matrix) - 1, 0

        while row > -1 and col < len(matrix[0]):
            val = matrix[row][col]
            if val > target: row -= 1 # Go up if current value too large
            elif val < target: col += 1 # Go right if current value too small
            else: return True

        return False

# Binary search version
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # Time: O(log(mn))
        # Space: O(1)

        # If target not in matrix
        if target < matrix[0][0] and target > matrix[-1][-1]: return False

        rowCount, colCount = len(matrix), len(matrix[0])
        left, right = 0, rowCount * colCount - 1

        def calculateIdx(mid) -> [int, int]:
            #                               rounded up | take remainder
            # get 4-idx number -> matrix[2][0] -> 4 // 4, 4 % 4
            # get 5-idx number -> matrix[2][1] -> 5 // 4, 5 % 4
            # get 6-idx number -> matrix[2][2] -> 6 // 4, 6 % 4
            # get 7-idx number -> matrix[2][3] -> 7 // 4, 7 % 4
            # get 8-idx number -> matrix[3][0] -> 8 // 4, 8 % 4
            # get 9-idx number -> matrix[3][1] -> 9 // 4, 9 % 4
            return mid // colCount, mid % colCount

        while left <= right:
            # Calculate idx
            mid = (left + right) // 2
            row, col = calculateIdx(mid)
            val = matrix[row][col]

            if val > target: right = mid - 1
            elif val < target: left = mid + 1
            else: return True

        return False
        

