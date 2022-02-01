class Solution:
    def partition(self, s: str) -> List[List[str]]:
        #Time: O(2^n)
        #Space: O(2^n)
        #Essentially how many ways are there to chop the string into smaller chunks of palindromes
        
        def solve(idx, current):
            if idx >= len(s):
                output.append(current)
                
            else:
                for subIdx in range(idx, len(s)):
                    newString = s[idx : subIdx + 1]
                    
                    if isPalindrome(newString):
                        solve(subIdx + 1, current + [newString])
            
            
        output = []
        solve(0, [])
        return output
    
def isPalindrome(s):
    
    left, right = 0, len(s) - 1
    
    while left < right:
        if s[left] != s[right]:
            return False
        
        left += 1; right -= 1
    
    return True