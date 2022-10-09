class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        # Time: O(mn)
        # Space: O(mn)
        
        # Solution:
        # Simulate gravity
        # Init a new array with its dimensions swapped
        # Migrate content to the new array
        
        #  l
        #           r        
        # ["#","#","*",".","*","."]
        # ["#","#","#","*",".","."]  <<<<
        # [".",".","#","#","#","#"]  
        
        # Simulate gravity with two pointers
        for row in box:
            r = len(row) - 1
            
            for l in range(len(row) - 1, -1, -1):
                # Obstacle
                if row[l] == '*':
                    r = l - 1
                
                # Stone
                elif row[l] == '#':
                    row[r], row[l] = row[l], row[r]
                    r -= 1
                    
        # Init a new array with its dimensions swapped            
        new_box = [[None for _ in range(len(box))] for _ in range(len(box[0]))]
        
        # Migrate content to the new array
        for r in range(len(box[0])):
            for c in range(len(box)):
                new_box[r][c] = box[len(box) - c - 1][r]
        
        return new_box
    