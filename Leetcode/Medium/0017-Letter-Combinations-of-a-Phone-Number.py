class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        #Time: O(4^n * n) As we have 4 letters with 4 possibilities at most, and n base cases to hit
        #Space: O(4^n * n) Recursive call-stack
        
        if digits == '': return []
        
        generate(output := [], '', digits)
        return output
    
def generate(output, current, digits):
    numToLetter = {'1':'1',
                   '2':'abc',
                   '3':'def',
                   '4':'ghi',
                   '5':'jkl',
                   '6':'mno',
                   '7':'pqrs',
                   '8':'tuv',
                   '9':'wxyz',
                   '0':'0'
    }
    
    if digits == '':
        output.append(current)
    else:
        #Use the first letter to find the possible combinations
        allChars = numToLetter[digits[0]] 
        for char in allChars:
            #Attach and eliminate said letter once we've used it
            generate(output, current + char, digits[1:])