class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        #Time: O(n)
        #Space: O(n)
        #Same idea as 'Isomorphic Strings'
        
        words = list(s.split(' '))
        
        if len(words) != len(pattern): return False
        
        wordsToPattern = {}
        patternToWords = {}
        
        for word, pat in zip(words, pattern):
            
            if word in wordsToPattern and wordsToPattern[word] != pat:
                return False
            
            if pat in patternToWords and patternToWords[pat] != word:
                return False
            
            wordsToPattern[word] = pat
            patternToWords[pat] = word
        
        return True