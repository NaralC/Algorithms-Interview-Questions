class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        #Time: O(n)
        #Space: O(n)
        
        output, count = '', 0
        
        for idx in reversed(range(len(s))):
            if s[idx] == '-':
                continue
                
            if count == k:
                output = '-' + output
                count = 0
            
            count += 1
            output = s[idx].upper() + output
        
        return output