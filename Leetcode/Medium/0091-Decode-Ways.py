class Solution:
    def numDecodings(self, s: str) -> int:
        #Time: O(n)
        #Space: O(n)
        
        if not s or s[0] == '0':
            return 0
        
        ways = [0 for _ in range(len(s) + 1)]
        ways[0] = 1
        ways[1] = 1
        
        for idx in range(2, len(s) + 1):
            oneChar = s[idx - 1 : idx]
            twoChar = s[idx - 2 : idx]
            
            if 0 < int(oneChar) <= 9:
                ways[idx] += ways[idx - 1]
            
            if 10 <= int(twoChar) <= 26:
                ways[idx] += ways[idx - 2]
                
        return ways[-1]