class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # Time: O(4^n) there are 4 decisions to make for each number
        # Space: O(n)
        
        lookup = {'2': 'abc', '3': 'def', '4': 'ghi', '5':'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
        
        def shuffle(idx, current):
            if idx >= len(digits):
                output.append(''.join(current))
                return
            
            nums = lookup[digits[idx]]
            for num in nums:
                shuffle(idx + 1, current + [num])   
        
        output = []
        shuffle(0, [])
        return output if len(digits) else []