class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        #Time: O(m) where m = length of the shortest word
        #Space: O(1)
        
        match = ''
        
        for idx in range(len(strs[0])):
            baseLine = strs[0][idx]
            
            for word in strs[1:]:
                if idx >= len(word) or baseLine != word[idx]:
                    return match
            
            match += baseLine
        
        return match