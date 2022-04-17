class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Time: O(n)
        # Space: O(n)
        
        longest = 0
        left = 0
        seen = set()
        
        for right in range(len(s)):
            # Keep sliding our window from the left until there's no duplicates
            while s[right] in seen:
                seen.remove(s[left])
                left += 1
                
            # Update variables
            seen.add(s[right])
            longest = max(longest, right - left + 1)
        
        return longest