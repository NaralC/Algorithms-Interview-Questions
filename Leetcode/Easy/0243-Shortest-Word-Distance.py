class Solution:
    def shortestDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        #Time: O(n)
        #Space: O(n)
        
        lastSeen = dict()
        output = float('inf')
        
        for idx, word in enumerate(wordsDict):
            #Put word into hash table
            if word in {word1, word2}:
                lastSeen[word] = idx
            
            #Update output when both words are present in our hash table
            if word1 in lastSeen and word2 in lastSeen:
                output = min(output, abs(lastSeen[word1] - lastSeen[word2]))
        
        return output