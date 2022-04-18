from collections import defaultdict

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # Time: O(n)
        # Space: O(n)
        
        lookup = defaultdict(int) # Tracks the frequency of each element present in current substring
        longest = 0 # The output
        
        left = 0
        for right in range(len(s)):
            # Add a new char to current substring
            lookup[s[right]] += 1
            
            # Shrink the substring/sliding window if other frequencies aside from the highest one exceed our replacement quota
            # Check this by subtracting the highest frequency from the length of current substring
            while (right - left + 1) - max(lookup.values()) > k:
                lookup[s[left]] -= 1
                left += 1
            
            # Update output
            longest = max(longest, right - left + 1)
        
        return longest