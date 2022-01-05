class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        #Time: O(4^(m * n)) since we're making 4 function calls each recursion
        #Space: O(4^(m * n))
        
        ROWS, COLS = len(board), len(board[0])
        visited = [[False for _ in range(COLS)] for _ in range(ROWS)]
        
        def traverse(row, col, idx):
            #Idx goes out of bound -> we've check all chars in word
            if idx > len(word) - 1:
                return True
            
            #Goes out of bound or is already visited
            if row < 0 or col < 0 or row >= ROWS or col >= COLS or visited[row][col] or word[idx] != board[row][col]:
                return False
            
            #Recursively proceed with DFS
            visited[row][col] = True
            top = traverse(row - 1, col, idx + 1)
            bot = traverse(row + 1, col, idx + 1)
            left = traverse(row, col - 1, idx + 1)
            right = traverse(row, col + 1, idx + 1)
            visited[row][col] = False
            
            return top or bot or left or right
        
        for row in range(ROWS):
            for col in range(COLS):
                if traverse(row, col, 0):
                    return True
        return False