class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        #Time: O(n)
        #Space: O(n)
        #Same idea as 'Word Pattern'
        
        s_to_t = {}
        t_to_s = {}
        
        for charS, charT in zip(s, t):
            
            if charS in s_to_t and s_to_t[charS] != charT:
                return False
            
            if charT in t_to_s and t_to_s[charT] != charS:
                return False
            
            s_to_t[charS] = charT
            t_to_s[charT] = charS
        
        return True