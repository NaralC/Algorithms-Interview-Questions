from collections import deque

class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        # Time: O(mn)
        # Space: O(mn)
        # Traverse through the rooms, get the locations of gates, and simultaneously perform BFS
        
        def getNeighbor(row, col):
            # Prevent boundary break
            if row < 0 or col < 0 or row >= len(rooms) or col >= len(rooms[0]):
                return
            
            # Prevent repeated work and running into walls
            if (row, col) in visited or rooms[row][col] == -1:
                return
            
            visited.add((row, col))
            q.append((row, col))
        
        # Get the locations of gates
        q = deque()
        visited = set()
        
        for row in range(len(rooms)):
            for col in range(len(rooms[0])):
                if not rooms[row][col]:
                    q.append((row, col))
                    visited.add((row, col))
        
        # Perform simultaneous BFS
        distance = 0
        
        while len(q):
            for _ in range(len(q)):
                # Assign distance to cell
                row, col = q.popleft()
                rooms[row][col] = distance
                
                # Append its neighbors
                getNeighbor(row + 1, col)
                getNeighbor(row, col + 1)
                getNeighbor(row - 1, col)
                getNeighbor(row, col - 1)
                
            distance += 1