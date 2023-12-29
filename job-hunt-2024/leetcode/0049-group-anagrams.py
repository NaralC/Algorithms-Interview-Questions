from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Time: O(nm)
        # Space: O(26)
        # where n = len(strs), m = max length of the words

        # Count each by their alphabet frequency
        # since the words are only in English lowercases

        counter = defaultdict(list)

        for word in strs:
            freq = [0 for _ in range(26)] # from a-z
            
            for char in word:
                freq[ord(char) - 97] += 1
            
            counter[tuple(freq)].append(word)

        return counter.values()
