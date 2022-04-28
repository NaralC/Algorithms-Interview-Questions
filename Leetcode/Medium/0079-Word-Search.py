class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # Time: O(4^(mn)) as we have 4 function calls at each cell
        # Space: O(4^(mn)) 
        
        def dfs(row, col, idx):
            # Check for current word's validity
            if idx > len(word) - 1:
                return True
            
            # Prevent infinite loop, boundary break, and char mismatch
            if (row, col) in seen:
                return
            
            if row < 0 or col < 0 or row >= len(board) or col >= len(board[0]):
                return
            
            if word[idx] != board[row][col]:
                return
            
            # Continue DFS
            seen.add((row, col))
            idx += 1
            
            if dfs(row + 1, col, idx): return True
            if dfs(row, col + 1, idx): return True
            if dfs(row - 1, col, idx): return True
            if dfs(row, col - 1, idx): return True
            
            # Relax cell to let other searches use it
            seen.remove((row, col))
        
        seen = set()
        
        for row in range(len(board)):
            for col in range(len(board[0])):
                if dfs(row, col, 0):
                    return True
                    
        return False