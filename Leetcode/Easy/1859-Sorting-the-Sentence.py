class Solution:
    def sortSentence(self, s: str) -> str:
        #Time: O(n)
        #Space: O(n)
        
        #Map words to their respective idx
        idxToWord = dict()
        
        for word in s.split(' '):
            idxToWord[int(word[-1])] = word[:-1]
        
        #Turn the map into a string
        output = [None for _ in range(len(idxToWord))]
        
        for idx, word in idxToWord.items():
            output[idx - 1] = word
        
        return ' '.join(output)