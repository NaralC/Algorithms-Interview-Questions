class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        #Time: O(m * n) iterating through every single element
        #Space: O(m * n) worst case where the entire board is purely made of O's
        
        #Traverse the border and capture any spots connected to border O's witn DFS
        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col] == 'O' and (row in [0, len(board) - 1] or col in [0, len(board[0]) - 1]):
                    capture(row, col, board)
                    
        #Flip uncaptured spots, as they are not connected to any border O's
        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col] == 'O':
                    board[row][col] = 'X'
        
        #Turn back captured spots to the original state
        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col] == 'C':
                    board[row][col] = 'O'
    
def capture(row, col, board):
    #Boundary check
    if row < 0 or row > len(board) - 1 or col < 0 or col > len(board[0]) - 1:
        return
    #Keep the spreading process within O's and connected spots
    if board[row][col] != 'O':
        return
    
    board[row][col] = 'C' #C = Captured
    capture(row - 1, col, board) #Capture neighboring spots
    capture(row + 1, col, board)
    capture(row, col - 1, board)
    capture(row, col + 1, board)
        