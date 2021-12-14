class Solution:
    def judgeCircle(self, moves: str) -> bool:
        return twoVariables(moves)

def twoVariables(moves):
    #Time: O(n)
    #Space: O(1)
    
    x, y = 0, 0
    
    for char in moves:
        if char == 'U':
            y += 1
        elif char == 'D':
            y -= 1
        elif char == 'L':
            x -= 1
        elif char == 'R':
            x += 1
        
    return x == y == 0
    
def hashTable(moves):
    #Time: O(n)
    #Space: O(n)
    
    directions = {'U': 0, 'D': 0, 'L': 0, 'R': 0}

    for char in moves:
        directions[char] += 1

    return directions['U'] == directions['D'] and directions['L'] == directions['R']