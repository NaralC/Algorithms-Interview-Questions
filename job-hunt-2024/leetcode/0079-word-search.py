class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # Time: O(n^2)
        # Space: O(n)
        
        seen = set() # Prevents re-using a cell by checking coordinates

        def DFS(row, col, idx):
            # Check current string
            if idx >= len(word): return True

            # Prevent out-of-bounds error
            if row < 0 or col < 0 or row > len(board) - 1 or col > len(board[0]) - 1:
                return False

            # Prevent infinite recursion
            if (row, col) in seen: return False
            
            # Check current string
            if word[idx] != board[row][col]: return False

            # THIS BEING BEORE THE CHUNK ABOVE FAILS 1/3 OF THE TEST CASES
            # since cells wouldn't be relaxed
            seen.add((row, col))

            l = DFS(row, col - 1, idx + 1) # Left
            r = DFS(row, col + 1, idx + 1) # Right
            t = DFS(row - 1, col, idx + 1) # Top
            b = DFS(row + 1, col, idx + 1) # Bottom

            # Let other recursions use the cell
            seen.remove((row, col))
            return l or r or t or b

        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col] == word[0] and DFS(row, col, 0): return True

        return False
