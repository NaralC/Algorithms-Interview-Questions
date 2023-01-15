class Solution:
    def minFlips(self, target: str) -> int:
        # Time: O(n)
        # Space: O(1)
        
        flips = 0
        current = '0'
        
        for num in target:
            if num != current:
                flips += 1
                current = '0' if current == '1' else '1'
                
        return flips
