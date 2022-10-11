class Solution:
    def candyCrush(self, board: List[List[int]]) -> List[List[int]]:
        # Time: O(mn)
        # Space: O(mn)
        
        while True:
            # Flag cells for deletion
            # - Look for vertical connections of size 3
            # - Look for horizontal connections of size 3
            crush = set()
            
            for r in range(len(board)):
                for c in range(len(board[0])):
                    if r >= 2 and board[r][c] and board[r][c] == board[r - 1][c] == board[r - 2][c]:
                        crush.add((r, c))
                        crush.add((r - 1, c))
                        crush.add((r - 2, c))
                        
                    if c >= 2 and board[r][c] and board[r][c] == board[r][c - 1] == board[r][c - 2]:
                        crush.add((r, c))
                        crush.add((r, c - 1))
                        crush.add((r, c - 2))
                        
            # Delete flagged cells
            if not len(crush): break
            
            for r, c in crush:
                board[r][c] = 0
            
            # Simulate gravity with two pointers
            for c in range(len(board[0])):
                bot = len(board) - 1
                
                for top in reversed(range(len(board))):
                    if board[top][c]:
                        board[top][c], board[bot][c] = board[bot][c], board[top][c]
                        bot -= 1
                    
        return board
    