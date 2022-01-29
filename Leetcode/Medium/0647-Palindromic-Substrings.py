class Solution:
    def countSubstrings(self, s: str) -> int:
        #Time: O(n^2)
        #Space: O(1)
        
        count = 0
        
        for idx in range(len(s)):
            #Odd cases like 'aba' (both ptrs start on the same middle)
            count += countPalindrome(idx, idx, s)
            
            #Even cases like 'abba' (one ptr starts on the middle, while the other starts to its right)
            count += countPalindrome(idx, idx + 1, s)
            
        return count
    
def countPalindrome(left, right, s):
    #Time: O(n)
    #Space: O(1)
    result = 0
    
    while left > -1 and right < len(s):
        if s[left] != s[right]:
            break

        #A string of length 1 always counts as a palindrome    
        result += 1
        left -= 1
        right += 1
        
    return result