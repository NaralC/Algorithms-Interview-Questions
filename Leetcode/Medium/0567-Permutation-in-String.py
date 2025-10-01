from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # Time: O(nm)
        # Space: O(n + m)
        lookupS1, lookupS2 = Counter(s1), Counter(s2[:len(s1)])

        #                  l
        # s1 = "ab", s2 = "eidbaooo"
        #                   r
        l, r = 0, len(s1) - 1

        while r < len(s2) - 1:
            # Compare
            if lookupS1 == lookupS2: return True

            # Expand window to the right
            r += 1
            lookupS2[s2[r]] += 1

            # Shrink window from the left
            if lookupS2[s2[l]] > 0: lookupS2[s2[l]] -= 1
            if lookupS2[s2[l]] <= 0: del lookupS2[s2[l]]
            l += 1

        return lookupS1 == lookupS2


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # Time: O(n)
        # Space: O(1)
        
        if len(s1) > len(s2): return False
        
        # Check and count the frequency of the first len(s1)
        freq1, freq2 = [0] * 26, [0] * 26
        
        for idx in range(len(s1)):
            freq1[ord(s1[idx]) - ord('a')] += 1
            freq2[ord(s2[idx]) - ord('a')] += 1
        
        if freq1 == freq2:
            return True
        
        # Skip the first len(s1) chars, and keep sliding a window of size len(s1) to the right
        left = 0; right = len(s1)
        
        while right < len(s2):
            # Check the hashtables together
            if freq1 == freq2:
                return True
            
            # Remove the left most char from s2
            freq2[ord(s2[left]) - ord('a')] -= 1
            
            # Add a new char to s2
            freq2[ord(s2[right]) - ord('a')] += 1
            
            left += 1; right += 1
            

        return freq1 == freq2
