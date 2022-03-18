class Solution:
    def customSortString(self, order: str, s: str) -> str:
        #Time: O(n)
        #Space: O(n)
        from collections import defaultdict
        
        #Use a map to check the frequency of each char in s
        freq = defaultdict(int)
        
        for char in s:
            freq[char] += 1
        
        #Form the final output
        output = []
        
        #First, append chars present in both s and order
        for char in order:
            if char in freq:
                output.append(freq[char] * char)
                del freq[char]
        
        #Secondly, append chars only present in s
        for char, val in freq.items():
            output.append(char * val)
        
        return ''.join(output)