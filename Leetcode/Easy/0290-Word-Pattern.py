class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        #Time: O(n)
        #Space: O(n)
        
        words = list(s.split(' '))
        if len(pattern) != len(words): return False
        
        matcher = {} #Pattern : Word
        
        for idx in range(len(words)):
            #Case1: pattern not in matcher
            if pattern[idx] not in matcher.keys():
                
                if words[idx] in matcher.values():
                    return False
                else:
                    matcher[pattern[idx]] = words[idx]
            
            #Case2: pattern already in matcher, but word mismatch
            elif matcher[pattern[idx]] != words[idx]:
                return False
                
        return True