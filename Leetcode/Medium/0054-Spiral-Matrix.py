class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        #Time: O(height * width)
        #Space: O(height * width)
        
        height, width = len(matrix), len(matrix[0])
        output = []
        left, right = 0, width - 1
        top, bot = 0, height - 1
        
        while left < right and top < bot:
            #Top left -> top right
            for col in range(left, right):
                output.append(matrix[top][col])
            
            #Top right -> bot right
            for row in range(top, bot):
                output.append(matrix[row][right])
                
            #Bot right -> bot left
            for col in range(right, left, -1):
                output.append(matrix[bot][col])
                
            #Bot left -> top left
            for row in range(bot, top, -1):
                output.append(matrix[row][left])
            
            left += 1
            right -= 1
            top += 1
            bot -= 1
        
        #Edge case: a leftover row or column in the middle
        #Perform a scan, any order is fine because the leftover is either a row/column
        if len(output) < width * height:
            for row in range(top, bot + 1):
                for col in range(left, right + 1):
                    output.append(matrix[row][col])
        
        return output
