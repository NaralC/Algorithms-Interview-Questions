class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        #Time: O(n)
        #Space: O(n)
        idx = len(digits) - 1
        addOne = 1
        
        #Keep looping as long as there's a carry and still in bound
        while addOne and idx >= 0:
            digits[idx] += addOne
            
            if digits[idx] > 9:
                digits[idx] -= 10
                addOne = 1
            else:
                addOne = 0
            
            idx -= 1
            
        if addOne: #Append 1 to beginning in case there's a carry left over
            digits.insert(0, 1)
        
        return digits