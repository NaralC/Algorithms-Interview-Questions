class Solution:
    def reverseVowels(self, s: str) -> str:
        #Time: O(n)
        #Space: O(n)
        
        vowels = {'a', 'e', 'i', 'o', 'u'}
        
        left, right = 0, len(s) - 1
        s = list(s)
        
        while left < right:
            #Case1: swap when left and right are pointing at vowels
            if s[left].lower() in vowels and s[right].lower() in vowels:
                s[left], s[right] = s[right], s[left]
                left += 1
                right -= 1
            
            #Case2: when left is not pointing at a vowel, move it
            elif s[left].lower() not in vowels:
                left += 1
            
            #Case3: when right is not pointing at a vowel, move it
            elif s[right].lower() not in vowels:
                right -= 1
            
        return ''.join(s)