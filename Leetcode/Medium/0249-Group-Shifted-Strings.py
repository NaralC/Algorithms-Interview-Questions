from collections import defaultdict

class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        # Time: O(nk) where n = number of words, k = length of longest word
        # Space: O(n)
        
        # Maps alphabets to their order (i.e., 'a' : 1, 'b' : 2)
        charToNum = {chr(num) : int(str(num - 96)) for num in range(97, 123)}
        
        # Group words by their shifting sequence
        group = defaultdict(list)
        
        for word in strings:
            sequence = []
            
            for idx in range(1, len(word)):
                prev, curr = word[idx - 1], word[idx]
                sequence.append((charToNum[prev] - charToNum[curr]) % 26)
            
            group[tuple(sequence)].append(word)
        
        return group.values()