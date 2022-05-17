class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        # Time: O(n)
        # Space: O(n)
        
        if len(palindrome) < 2:
            return ''
        
        # Replace with 'a' as far left as possible to minimize the lexicographical size
        p = list(palindrome)
        
        for idx in range(len(p) // 2):
            if p[idx] != 'a':
                p[idx] = 'a'
                return ''.join(p)
        
        # Replace with 'b' as far right as it minimizes the lexicographical size
        # and prevent palindrome in case of strings entirely made of 'a'
        p[-1] = 'b'
        return ''.join(p)