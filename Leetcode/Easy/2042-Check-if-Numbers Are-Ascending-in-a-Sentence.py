class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        #Time: O(n)
        #Space: O(n)
        
        #Retrieve only numbers (be careful non-single digits)
        onlyNums = [int(char) for char in s.split(' ') if char.isnumeric()]
        
        #Check whether the numbers are strictly increasing
        for idx in range(1, len(onlyNums)):
            if onlyNums[idx - 1] >= onlyNums[idx]:
                return False
        
        return True