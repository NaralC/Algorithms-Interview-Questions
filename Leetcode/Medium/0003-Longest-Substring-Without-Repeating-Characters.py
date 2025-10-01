class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Time: O(n)
        # Space: O(n)
        seen = set()
        longest = 0
        l, r = 0, 0

        while r < len(s):
            # New char, not a dupe. Extend window to right
            if s[r] not in seen:
                seen.add(s[r])
                longest = max(longest, len(seen)) # update length
                r += 1

            # New char, already existing. Shrink window from left
            elif s[r] in seen:
                seen.remove(s[l])
                l += 1

        return longest
        
