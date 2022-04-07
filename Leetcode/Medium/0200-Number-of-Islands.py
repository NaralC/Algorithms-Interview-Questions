from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # Time: O(mn)
        # Space: O(mn)
        # Iterate through all cells -> Sink an island if we counter one with DFS/BFS
        
        count = 0
        
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == '1':
                    count += 1
                    
                    # Pick a flood-fill algorithm
                    bfs(row, col, grid)
                    dfs(row, col, grid)
        
        return count
    
def dfs(row, col, grid):
    # Prevent boundary break and only sink '1' cells
    if row < 0 or col < 0 or row >= len(grid) or col >= len(grid[0]) or grid[row][col] != '1':
        return

    # Sink the current cell
    grid[row][col] = '0'

    # Continue sinking its neighboring cells
    dfs(row + 1, col, grid)
    dfs(row - 1, col, grid)
    dfs(row, col + 1, grid)
    dfs(row, col - 1, grid)

def bfs(a, b, grid):
    q = deque([(a, b)])

    while len(q):
        # Sink current cell and continue BFS (only if it's '1')
        row, col = q.popleft()

        if grid[row][col] == '1':
            grid[row][col] = '0'

            # Push its neighbors into q
            if row > 0: q.append((row - 1, col)) # Top

            if row < len(grid) - 1: q.append((row + 1, col)) # Bot

            if col > 0: q.append((row, col - 1)) # Left

            if col < len(grid[0]) - 1: q.append((row, col + 1)) # Right
                