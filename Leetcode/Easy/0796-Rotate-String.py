class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        #Time: O(n^2)
        #Space: O(n)

        #If they aren't anagrams, then it's impossible to rotate s to match goal
        if sorted(s) != sorted(goal): return False
        
        #Try every possibility, with len(s) rotations
        for k in range(len(s)):
            if goal == rotate(s, k):
                return True
            
        return False
    
def rotate(s, numberOfRotations):
    #Time: O(n)
    #Space: O(n)
    
    output = list(s)
    
    for idx, char in enumerate(s):
        newIdx = (idx + numberOfRotations) % len(s)
        output[newIdx] = char
    
    return ''.join(output)