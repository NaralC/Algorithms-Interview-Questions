class Solution:
    def countSegments(self, s: str) -> int:
        #Time: O(n)
        #Space: O(1)
        #The start of a word indicates that there's a segment to the left, like in 'Longest Consecutive Sequence'
        
        count = 0
        
        for idx in range(len(s)):
            #There's a segment to our left / Handle the first word / If there are only spaces in the string
            if not s[idx].isspace() and (s[idx - 1].isspace() or idx == 0):
                count += 1
        
        return count