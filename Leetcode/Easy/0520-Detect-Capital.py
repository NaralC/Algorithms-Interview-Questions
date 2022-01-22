class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        #Time: O(n)
        #Space: O(1)
        
        if len(word) <= 1: return True        

        startsWithCapital = word[0].isupper()
        continuesToBeCapital = word[1].isupper()
        
        for idx in range(1, len(word)):
        #Case1: 'a...' starts with lower, but followed by upper
            if not startsWithCapital and word[idx].isupper():
                return False
            
        #Case2: 'AA...' followed by lower
            if startsWithCapital and continuesToBeCapital and word[idx].islower():
                return False
            
        #Case3: 'Aa...' followed by upper
            if startsWithCapital and not continuesToBeCapital and word[idx].isupper():
                return False
            
        return True