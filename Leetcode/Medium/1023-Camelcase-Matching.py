class Solution:
    def camelMatch(self, queries: List[str], pattern: str) -> List[bool]:
        #Time: O(n * m) where n = len(queries), m = length of the longest word in queries
        #Space: O(n)
        
        def check(word):
            #Count how many capital letters there are in the current query
            wordCapital = 0
            
            for char in word:
                if char.isupper():
                    wordCapital += 1
            
            #If the capital count is different, return False
            #This automatically takes care of random capital letters inserted to the back
            if wordCapital != patternCapital: return False
            
            #Deploy two pointers for generic string matching
            patternPtr = 0
            
            for wordPtr in range(len(word)):
                #The string matching validates if the pattern ptr goes ouf of bound
                if patternPtr >= len(pattern):
                    break
                
                #If there's match, increment our pattern ptr
                if word[wordPtr] == pattern[patternPtr]:
                    patternPtr += 1
            
            return patternPtr >= len(pattern)
        
        #Count how many capital letters there are in pattern
        patternCapital = 0
        for char in pattern:
            if char.isupper():
                patternCapital += 1
        
        #Check every single query against the pattern
        output = [False for _ in range(len(queries))]
        for idx, word in enumerate(queries):
            if check(word):
                output[idx] = True
        
        return output