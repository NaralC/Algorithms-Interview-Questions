class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxLen = 0
        seen = set()
        l, r = 0, 0

        while r < len(s):
            # New char, not a dupe
            if s[r] not in seen:
                seen.add(s[r])
                maxLen = max(maxLen, len(seen))
                r += 1

            # New char, is a dupe
            elif s[r] in seen:
                seen.remove(s[l])
                l += 1

        return maxLen
        
