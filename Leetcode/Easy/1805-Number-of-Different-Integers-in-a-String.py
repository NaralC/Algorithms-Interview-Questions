class Solution:
    def numDifferentIntegers(self, word: str) -> int:
        #Time: O(n)
        #Space: O(n)
        
        mode = 'digit' if word[0].isdigit() else 'word'
        seen = set()
        
        slow, fast = 0, 0
        
        while fast < len(word):
            
            if mode == 'digit' and word[fast].isalpha():
                seen.add(int(word[slow : fast]))
                slow = fast
                mode = 'word'
            
            elif mode == 'word' and word[fast].isdigit():
                slow = fast
                mode = 'digit'
                
            fast += 1
        
        #Take care of the last chunk of string
        if (last := word[slow : fast]).isdigit():
            seen.add(int(last))
        
        return len(seen)