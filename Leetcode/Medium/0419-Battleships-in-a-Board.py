class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        return greedy(board)
        
def greedy(board):
    #Time: O(m * n)
    #Space: O(1)

    def checkNeighbor(row, col):
        #We only need to count the top left cell of each ship because of how they are shaped
        #Top left cell = (Nothing to the left) & (Nothing to the top)

        if (row == 0 or board[row - 1][col] == '.') and (col == 0 or board[row][col - 1] == '.'):
            return True

    count = 0

    for row in range(len(board)):
        for col in range(len(board[0])):
            if board[row][col] == 'X' and checkNeighbor(row, col):
                count += 1

    return count
        
def dfs(board):
    #Time: O(m * n)
    #Space: O(m * n)
    
    def sinkShip(row, col):
        #Prevent boundary break
        if row < 0 or col < 0 or row >= len(board) or col >= len(board[0]):
            return

        #Keep the sinking process inside the current ship
        if board[row][col] != 'X':
            return

        board[row][col] = '.' #Sink current cell

        sinkShip(row - 1, col)
        sinkShip(row + 1, col)
        sinkShip(row, col - 1)
        sinkShip(row, col + 1)

    count = 0

    for row in range(len(board)):
        for col in range(len(board[0])):
            if board[row][col] == 'X':
                count += 1
                sinkShip(row, col)

    return count