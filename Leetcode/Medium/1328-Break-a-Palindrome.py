class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        # Time: O(n)
        # Space: O(n)
        
        if len(palindrome) == 1:
            return ''
        
        # Lexicographically smallest, start with 'a'
        # Replace any char as far left with 'a'
        palindrome = list(palindrome)
        
        for idx in range(len(palindrome) // 2):
            if palindrome[idx] != 'a':
                palindrome[idx] = 'a'
                return ''.join(palindrome)
        
        # If the entire string is strictly made of 'a'
        palindrome[-1] = 'b'
            
        return ''.join(palindrome)