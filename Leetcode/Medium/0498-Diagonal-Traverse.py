from collections import defaultdict

class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        # Time: O(nlogn) where n = number of cells
        # Space: O(n)
        
        # Group numbers by the sum of their indices
        group = defaultdict(list)
        
        for row in range(len(mat)):
            for col in range(len(mat[0])):
                group[row + col].append(mat[row][col])
        
        # Return the numbers ordered by the sum of their indices
        output = []
        
        for idxSum, nums in sorted(group.items()):
            if idxSum % 2 == 0:
                output += nums[::-1]
            else:
                output += nums
                    
        return output