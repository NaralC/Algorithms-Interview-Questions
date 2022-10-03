class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def dfs(row, col, idx):
            # See if it's a match
            if idx == len(word):
                return True

            # Boundary breaks
            if row < 0 or col < 0 or row >= len(board) or col >= len(board[0]):
                return False

            # See if current cell's been used up or it's a mismatch
            if (row, col) in seen or board[row][col] != word[idx]:
                return False

            # Use up the current cell
            seen.add((row, col))
            idx += 1

            if dfs(row - 1, col, idx): return True
            if dfs(row + 1, col, idx): return True
            if dfs(row, col - 1, idx): return True
            if dfs(row, col + 1, idx): return True
        
            # Relax the current cell
            seen.remove((row, col))
        
    
        # "ABCCED" -> ["A", "B", ..., "D"]
        word = list(word)
        seen = set() # (row, col)

        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col] == word[0]:
                    if dfs(row, col, 0):
                        return True

        return False