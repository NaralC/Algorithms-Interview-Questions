class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        # Time: O(n)
        # Space: O(1)
        
        unmatchedOpen = unmatchedClose = 0
        
        for char in s:
            # Require a closing
            if char == '(':
                unmatchedOpen += 1
            
            # Require an opening
            else:
                # There's an opening already available
                if unmatchedOpen >= 1:
                    unmatchedOpen -= 1 # Use it up to make a valid pair
                # There's no opening available
                else:
                    unmatchedClose += 1
        
        return unmatchedOpen + unmatchedClose