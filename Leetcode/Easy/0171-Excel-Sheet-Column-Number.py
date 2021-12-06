class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        #Time: O(n)
        #Space: O(1)
        output = 0
        multiplier = 1
        
        for idx in reversed(range(len(columnTitle))):
            output += multiplier * (ord(columnTitle[idx]) - 64)
            multiplier *= 26
            
        return output