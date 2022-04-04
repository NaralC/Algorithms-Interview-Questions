class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Time: O(n)
        # Space: O(1)
        
        # Words of different length cannot be anagrams
        if len(s) != len(t):
            return False
        
        # Return if both words have the same character count 
        s_count, t_count = [0] * 26, [0] * 26
        
        for s_char, t_char in zip(s, t):
            s_count[ord(s_char) - ord('a')] += 1
            t_count[ord(t_char) - ord('a')] += 1
        
        return s_count == t_count