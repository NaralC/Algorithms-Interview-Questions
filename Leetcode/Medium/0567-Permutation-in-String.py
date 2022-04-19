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