class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #Time: O(n)
        #Space: O(1)
        
        #[0, 0, 0, ...., z]
        #[a, b, c, ...., z]
        charFreq1 = [0 for _ in range(26)]
        charFreq2 = [0 for _ in range(26)]
        
        for idx, char in enumerate(s):
            #ord('a') - ord('a') = 96 - 96 = 0
            #charFreq1[0] += 1
            charFreq1[ord(char) - ord('a')] += 1
        
        for idx, char in enumerate(t):
            charFreq2[ord(char) - ord('a')] += 1
            
        return charFreq1 == charFreq2