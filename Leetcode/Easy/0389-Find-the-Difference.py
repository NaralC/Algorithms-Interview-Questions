class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        #Time: O(t) since len(t) > len(s)
        #Space: O(1) since there are only lowercase English alphabets
        
        #Use a makeshift hashtable to keep track of each alphabet's number of appearance
        s_alphabets = [0 for _ in range(26)]
        t_alphabets = [0 for _ in range(26)]
        
        for idx in range(len(t)):
            #Prevent idx out of bound since len(s) < len(t)
            if idx < len(s): 
                s_alphabets[ord(s[idx]) - ord('a')] += 1
                
            t_alphabets[ord(t[idx]) - ord('a')] += 1
            
        for idx in range(26):
            if s_alphabets[idx] != t_alphabets[idx]:
                return chr(ord('a') + idx)