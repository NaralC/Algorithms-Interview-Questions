class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # Time: O(nm)
        # Space: O(nm)
        
        def dfs(row, col):
            # Boundary check
            if row < 0 or col < 0 or row > len(grid) - 1 or col > len(grid[0]) - 1:
                return

            # Prevent visiting water body
            if grid[row][col] != '1': return
            grid[row][col] = '0'

            # Continue on
            dfs(row + 1, col)
            dfs(row - 1, col)
            dfs(row, col + 1)
            dfs(row, col - 1)

        def bfs(row, col):
            q = deque([(row, col)])

            while len(q):
                width = len(q)

                for _ in range(width):
                    r, c = q.popleft()

                    # Boundary check
                    if r < 0 or c < 0 or r > len(grid) - 1 or c > len(grid[0]) - 1: continue

                    # Prevent visiting water body
                    if grid[r][c] != '1': continue
                    grid[r][c] = '0'

                    # Continue on
                    q.append((r + 1, c))
                    q.append((r - 1, c))
                    q.append((r, c + 1))
                    q.append((r, c - 1))

        count = 0

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == '1':
                    bfs(row, col)
                    count += 1

        return count
