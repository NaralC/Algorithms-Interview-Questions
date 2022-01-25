class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        #Time: O(s) since s is shorter and we only need to traverse it
        #Space: O(1)
        
        #If the subseqence is longer than the other one, then it's no longer a subsequence
        if len(s) > len(t): return False
        
        ptrS, ptrT = 0, 0
        while ptrS < len(s) and ptrT < len(t):
            #Move up both ptrs if they match
            if s[ptrS] == t[ptrT]:
                ptrS += 1
                ptrT += 1
            
            #If not - only move up the ptr on t
            else:
                ptrT += 1
        
        #When we exit the loop, 2 things can happen:
        #1) ptrS is out of bound: completed the subsequence check
        #2) ptrT is out of bound: subsequence check uncompleted
        return True if ptrS >= len(s) else False