class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        # Time: O(n)
        # Space: O(n)
        
        # Every char must appear even number of times, except for odd-length strings where the middle element is available for one char
        foundOdd = False
        freq = Counter(s)
        
        for char, freq in freq.items():
            # Only process odd freq elements
            if freq % 2 == 1:
                if len(s) % 2 == 0 or foundOdd:
                    return False
                
                foundOdd = True
                
        return True