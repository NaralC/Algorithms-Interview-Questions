class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # Time: O(mn)
        # Space: O(mn)
        
        nums = []
        
        left, right = 0, len(matrix[0]) - 1
        top, bot = 0, len(matrix) - 1
        
        while left < right and top < bot:
            # Top left -> Top right
            for col in range(left, right):
                nums.append(matrix[top][col])
            
            # Top right -> Bot right
            for row in range(top, bot):
                nums.append(matrix[row][right])
            
            # Bot right -> Bot left
            for col in range(right, left, -1):
                nums.append(matrix[bot][col])
            
            # Bot left -> Top left
            for row in range(bot, top, -1):
                nums.append(matrix[row][left])
            
            # Move boundary inwards
            left += 1; right -= 1
            top += 1; bot -= 1
        
        # Take care of a row/col of elements left in the middle
        COLS, ROWS = len(matrix[0]), len(matrix)
        
        if len(nums) < COLS * ROWS:
            # Sweep top -> bot
            for row in range(top, bot + 1):
                # Sweep left -> right
                for col in range(left, right + 1):
                    nums.append(matrix[row][col])
        
        return nums