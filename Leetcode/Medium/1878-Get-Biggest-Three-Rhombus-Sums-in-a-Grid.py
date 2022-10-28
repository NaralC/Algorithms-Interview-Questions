class Solution:
    def getBiggestThree(self, grid: List[List[int]]) -> List[int]:
        # Time: O(?)
        # Space: O(?)
        
        output = []
        
        # 1x1, 3x3, 5x5, ...
        for size in range(1, min(len(grid), len(grid[0])) + 1, 2):
            for row in range(len(grid)):
                for col in range(len(grid[0])):
                    diameter = size // 2
                    
                    if not diameter:
                        output.append(grid[row][col])
                        continue
                        
                    total = 0
                    x, y = row, col + diameter
                    
                    for _ in range(diameter):
                        total += grid[x][y]
                        x += 1; y += 1
                    
                    for _ in range(diameter):
                        total += grid[x][y]
                        x += 1; y -= 1
                        
                    for _ in range(diameter):
                        total += grid[x][y]
                        x -= 1; y -= 1
                        
                    for _ in range(diameter):
                        total += grid[x][y]
                        x -= 1; y += 1
                    
                    output.append(total)
                        
        return sorted(output, reverse = True)
                    
                        