class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Time: O(n)
        # Space: O(1)

        l, r = 0, len(s) - 1

        while l < r:
            charL, charR = s[l].lower(), s[r].lower()

            if not charL.isalnum():
                l += 1
                continue
            if not charR.isalnum():
                r -= 1
                continue
            
            if charL != charR: return False
            l += 1; r -= 1

        return True
