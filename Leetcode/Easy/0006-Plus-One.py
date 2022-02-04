class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        #Time: O(n)
        #Space: O(1)
        
        for idx in reversed(range(len(digits))):
            #Non-9 numbers mean no carry over -> terminate
            if digits[idx] != 9:
                digits[idx] += 1
                return digits
            
            #9 means there's a leftover -> continue looping
            else:
                digits[idx] = 0
        
        #Reaching here -> there's a leftover
        return [1] + digits