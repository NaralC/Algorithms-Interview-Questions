class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        #Time: O(n + m)
        #Space: O(1)
        
        #Magazine's letter count has to be higher/equal to that of ransomNote
        #since magazine is used as a base to construct ransomNote
        
        alphabetCount = [0 for _ in range(26)]
        
        for char in magazine:
            alphabetCount[ord(char) - ord('a')] += 1
        
        for char in ransomNote:
            if alphabetCount[ord(char) - ord('a')] <= 0: return False
            
            alphabetCount[ord(char) - ord('a')] -= 1
            
        return True