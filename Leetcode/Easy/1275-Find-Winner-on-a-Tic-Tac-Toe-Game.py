class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        # Time: O(mn) m = number of moves, n = board size
        # Space: O(n^2)
        
        # At least 3 rounds must have passed to have a winner
        n = 3
        
        if len(moves) < n: return 'Pending'
          
        def checkRow(row, player):
            for col in range(n):
                if board[row][col] != player:
                    return False
            
            return True
        
        def checkCol(col, player):
            for row in range(n):
                if board[row][col] != player:
                    return False
            
            return True
        
        def checkDiag(player):
            for row in range(n):
                if board[row][row] != player:
                    return False
            
            return True
        
        def checkCounterDiag(player):
            for row in range(n):
                if board[row][n - 1 - row] != player:
                    return False
            
            return True
        
        # Check for winners every time a move is made
        board = [['' for _ in range(n)] for _ in range(n)]
        player = 1
        
        # Make them moves
        for row, col in moves:
            board[row][col] = player
            
            if (checkRow(row, player) or checkCol(col, player) or
               row == col and checkDiag(player) or row + col == n - 1 and checkCounterDiag(player)):
                return 'A' if player == 1 else 'B'
            
            player *= -1
        
        return 'Pending' if len(moves) < 9 else 'Draw'
    