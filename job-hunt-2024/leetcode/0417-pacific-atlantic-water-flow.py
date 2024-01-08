class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # Time: O(mn)
        # Space: O(mn)
        
        def dfs(r, c, prevHeight, seen):
            # Boundary
            if r < 0 or c < 0 or r > len(heights) - 1 or c > len(heights[0]) - 1:
                return

            # Height check
            if prevHeight > heights[r][c]:
                return

            # Prevent cycle
            if (r, c) in seen: return
            seen.add((r, c))

            # Continue
            dfs(r + 1, c, heights[r][c], seen)
            dfs(r - 1, c, heights[r][c], seen)
            dfs(r, c + 1, heights[r][c], seen)
            dfs(r, c - 1, heights[r][c], seen)

        # Start from the oceans instead, see which cells are reachable. Take the intersection
        pacific, atlantic = set(), set()

        for col in range(len(heights[0])):
            dfs(0, col, float('-inf'), pacific) # Top row
            dfs(len(heights) - 1, col, float('-inf'), atlantic) # Bot row

        for row in range(len(heights)):
            dfs(row, 0, float('-inf'), pacific) # Left col
            dfs(row, len(heights[0]) - 1, float('-inf'), atlantic) # Right col

        return pacific & atlantic
        