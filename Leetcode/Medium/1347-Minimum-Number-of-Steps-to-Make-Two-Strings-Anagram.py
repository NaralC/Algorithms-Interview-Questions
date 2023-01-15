from collections import Counter 

class Solution:
    def minSteps(self, s: str, t: str) -> int:
        # Time: O(n)
        # Space: O(n)
        
        # Subtract all shared chars from one string from the other, that's the answer
        # Both strings can play either role
        s_freq = Counter(s)
        
        for char in t:
            if char in s_freq and s_freq[char] > 0:
                s_freq[char] -= 1
                
        return sum(s_freq.values())
    
#     def minSteps(self, s: str, t: str) -> int:
#         # Time: O(n)
#         # Space: O(n)
        
#         # Replace only. No deletions or additions
#         s_freq = [0] * 26
#         t_freq = [0] * 26
        
#         for c1, c2 in zip(s, t):
#             s_freq[ord(c1) - ord('a')] += 1
#             t_freq[ord(c2) - ord('a')] += 1
            
#         # Count the diff between each element
#         output = 0
        
#         for c1, c2 in zip(s_freq, t_freq):
#             output += abs(c1 - c2) if c1 > c2 else 0
        
#         return output