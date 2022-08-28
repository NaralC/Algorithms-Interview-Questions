from collections import deque

class Solution:
    def sumZero(self, n: int) -> List[int]:
        # Time: O(n)
        # Space: O(n)
        
        output = deque()
        
        # Odd n -> expand from middle, but also take 0
        # Even n -> expand from middle, but leave out 0
        
        if isOdd(n): output.append(0)
        
        for idx in range(n // 2):
            output.append(idx + 1)
            output.appendleft(-idx - 1)
        
        return output
    
def isOdd(num):
    return num % 2 != 0