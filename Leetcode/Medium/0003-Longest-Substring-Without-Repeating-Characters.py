class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Time: O(n)
        # Space: O(n)

        substr = set()
        output = 0
        l = 0
        
        for r in range(len(s)):
            # Keep sliding our window to the right until there's no duplicate
            while s[r] in substr:
                substr.remove(s[l])
                l += 1
                
            # New addition
            substr.add(s[r])
            output = max(output, len(substr))
        
        return output
    