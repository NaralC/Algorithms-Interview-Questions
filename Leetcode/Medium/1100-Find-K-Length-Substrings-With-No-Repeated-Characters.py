from collections import Counter

class Solution:
    def numKLenSubstrNoRepeats(self, s: str, k: int) -> int:
        # Time: O(n)
        # Space: O(n)
        
        if len(s) < k: return 0
        
        window = Counter(s[:k])
        output = 1 if len(window.keys()) == k else 0
        
        for idx in range(k, len(s)):
            # Remove the leftmost char            
            window[s[idx - k]] -= 1
            
            if window[s[idx - k]] == 0:
                window.pop(s[idx - k])
            
            # Add a new char
            window[s[idx]] = window.get(s[idx], 0) + 1
            
            # Update output
            output += 1 if len(window.keys()) == k else 0
        
        return output
        