class Solution:
    def countSubstrings(self, s: str) -> int:
        # Time: O(n^2)
        # Space: O(1)
        
        def countPalindromes(l, r):
            result = 0

            while l > -1 and r < len(s):
                if s[l] != s[r]:
                    break

                result += 1
                l -= 1
                r += 1

            return result
    
        output = 0
        
        for idx in range(len(s)):
            # Odd cases like 'aba' (both ptrs start on the same middle)
            output += countPalindromes(idx, idx)
            
            # Even cases like 'abba' (one ptr starts on the middle, while the other starts to its right)
            output += countPalindromes(idx, idx + 1)
            
        return output
    
    
            