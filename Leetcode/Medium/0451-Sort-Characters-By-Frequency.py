from collections import Counter

class Solution:
    def frequencySort(self, s: str) -> str:
        #Time: O(nlogn)
        #Space: O(n)
        
        #Map each char's frequency to itself
        freq = Counter(s)
        
        #Sort based on frequency
        words = sorted(freq, key = lambda x: freq[x], reverse = True)
        
        #Form the final string and ship it
        output = []
        
        for char in words:
            output.append(freq[char] * char)
        
        return ''.join(output)