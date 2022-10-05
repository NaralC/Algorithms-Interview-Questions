from collections import defaultdict

class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        # Time: O(n)
        # Space: O(n)
        # where n = number of cells in matrix
        
        # Assuming:
        # - matrix is always valid (it's always n*n)
        # - all cells are filled with numbers that fit into memory
        
        # Solution:
        # Find n/max of matrix
        n = len(matrix)
        
        # Loop through matrix, have hashtable to track all rows and cols
        lookup_row = defaultdict(set)
        lookup_col = defaultdict(set)
        
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                lookup_row[r].add(matrix[r][c])
                lookup_col[c].add(matrix[r][c])
        
        # Check all values of hashtable has a length of n
        for _, val in lookup_row.items():
            if len(val) != n:
                return False
            
        for _, val in lookup_col.items():
            if len(val) != n:
                return False
            
        return True
    