from collections import deque

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        # Time: O(mn)
        # Space: O(mn)
        # Any 'O' that is not on the border and it is not connected to an 'O' on the border will be flipped to 'X'

#         def capture(row, col):
#             # Prevent boundary break
#             if row < 0 or col < 0 or row >= len(board) or col >= len(board[0]):
#                 return
            
#             # Only proceed if the current cell is an O
#             if board[row][col] != 'O':
#                 return
#             board[row][col] = 'C'
            
#             capture(row + 1, col)
#             capture(row - 1, col)
#             capture(row, col + 1)
#             capture(row, col - 1)
        
        def capture(a, b):
            q = deque()
            q.append((a, b))
            
            while len(q):
                # Only proceed if the current cell is an O
                row, col = q.popleft()
                
                if board[row][col] != 'O':
                    continue
                board[row][col] = 'C'
                
                # Append its neighbors back to q
                if row > 0: q.append((row - 1, col)) # Top
                    
                if row < len(board) - 1: q.append((row + 1, col)) # Right
                    
                if col > 0: q.append((row, col - 1)) # Left
                    
                if col < len(board[0]) - 1: q.append((row, col + 1)) # Bot
                    
        
        # Traverse the border -> Capture non-border O's connected to border ones
        for row in range(len(board)):
            for col in range(len(board[0])):
                if row == 0 or col == 0 or row == len(board) - 1 or col == len(board[0]) - 1:
                    if board[row][col] == 'O':
                        capture(row, col)
                        
        # Traverse the entire board -> Flip all O's into X's
        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col] == 'O':
                    board[row][col] = 'X'
        
        # Traverse the entire board -> Revert captured ('C') cells back to O's
        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col] == 'C':
                    board[row][col] = 'O'
        