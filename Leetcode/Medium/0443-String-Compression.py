class Solution:
    def compress(self, chars: List[str]) -> int:
        # Time: O(n)
        # Space: O(1)
        
        l = r = 0
        
        while r < len(chars):
            chars[l] = chars[r]
            count = 1
            
            while r + 1 < len(chars) and chars[r + 1] == chars[r]:
                r += 1
                count += 1
            
            if count > 1: 
                for c in str(count):
                    chars[l + 1] = c
                    l += 1
                
            r += 1
            l += 1
        
        return l
    