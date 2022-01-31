class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        #Time: O(m*n)
        #Space: O(1)
        
        highest = 0
        
        for account in accounts:
            current = 0
            
            for val in account:
                current += val
                
            highest = max(highest, current)
            
        return highest