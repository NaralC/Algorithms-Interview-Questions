class Solution:
    def candyCrush(self, board: List[List[int]]) -> List[List[int]]:
        # Time: O(mn)
        # Space: O(1)
        
        while True:
            # Flag candies for deletion
            # Check for connections of size 3
            flag = set()
            
            for r in range(len(board)):
                for c in range(len(board[0])):
                    # Horizontal connection
                    if r < len(board) - 2 and board[r][c] > 0 and board[r][c] == board[r + 1][c] == board[r + 2][c]:
                        flag |= {(r, c), (r + 1, c), (r + 2, c)}
                    
                    # Vertical connection
                    if c < len(board[0]) - 2 and board[r][c] > 0 and board[r][c] == board[r][c + 1] == board[r][c + 2]:
                        flag |= {(r, c), (r, c + 1), (r, c + 2)}
            
            # Check if board is stable
            if not len(flag): break
            
            # Delete the candies
            for r, c in flag:
                board[r][c] = 0
            
            # Simulate gravity
            for c in range(len(board[0])):
                bot = len(board) - 1
                
                for top in reversed(range(len(board))):
                    # Encounter candy
                    if board[top][c]:
                        board[top][c], board[bot][c] = board[bot][c], board[top][c]
                        bot -= 1
            
        return board
        