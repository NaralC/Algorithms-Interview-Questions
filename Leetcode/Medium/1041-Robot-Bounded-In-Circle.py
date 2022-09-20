class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        # Time: O(n) where n = len(instructions)
        # Space: O(1)
        
        # What constitutes as a cycle?
        # 1. End of instructions, the robot's back at the start
        # 2. End of instructions, the robot changes direction
        
        # 0 = North, 1 = East, 2 = South, 3 = West
        di = 0
        x = y = 0
        
        for i in instructions:
            if i == 'L':
                di += -1 if di > 0 else 3
            
            elif i == 'R':
                di += 1 if di < 3 else -3
            
            else:
                if di == 0:
                    y += 1
                elif di == 1:
                    x += 1
                elif di == 2:
                    y -= 1
                else:
                    x -= 1
                    
        if x == 0 and y == 0 or di != 0:
            return True
        
        return False