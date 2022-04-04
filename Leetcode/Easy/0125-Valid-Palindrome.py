class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Time: O(n)
        # Space: O(1)
        
        # Check by starting from the front and back simultaneously
        left, right = 0, len(s) - 1
        
        while left < right:
            # Skip on non-alnum chars first
            while left < right and not s[left].isalnum():
                left += 1

            while left < right and not s[right].isalnum():
                right -= 1
            
            # Return false if s invalidates as a palindrome
            if s[left].lower() != s[right].lower():
                return False
            
            # Move our ptrs inwards
            left += 1; right -= 1
            
        return True