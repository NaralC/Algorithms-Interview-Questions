from collections import defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Time: O(n)
        # Space: O(n)
        # where n = the bigger of both string's length

        # Check if same length
        if len(s) != len(t): return False

        # Char count should be identical, no values can be more than 0
        freq = defaultdict(int)

        for charS, charT in zip(s, t):
            freq[charS] += 1
            freq[charT] -= 1

        for key, value in freq.items():
            if value != 0: return False

        return True
