class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        #Time: O(n^m) where n = len(haystack), m = len(needle)
        #Space: O(1)
        
        if not len(needle): return 0
        elif not len(haystack): return -1

        for idx in range(len(haystack) - len(needle) + 1):
             if haystack[idx : idx + len(needle)] == needle:
                return idx
        
        return -1