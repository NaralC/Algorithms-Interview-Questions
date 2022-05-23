from collections import defaultdict

class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        # Time: O(mn)
        # Space: O(mn)
        
        # Group numbers by the difference of their indices (row - col)
        nums = defaultdict(set)
        
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                # The values in one group must all be identical to validate the matrix as Toeplitz
                # Also consider when starting out an empty set
                if not len(nums[row - col]) or matrix[row][col] in nums[row - col]:
                    nums[row - col].add(matrix[row][col])
                
                # Adding a different number to set
                else:
                    return False
                
        return True