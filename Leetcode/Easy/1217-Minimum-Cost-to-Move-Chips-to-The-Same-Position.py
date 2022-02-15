class Solution:
    def minCostToMoveChips(self, position: List[int]) -> int:
        #Time: O(n)
        #Space: O(1)
        
        even, odd = 0, 0
        
        for parity in position:
            #Even
            if parity % 2 == 0:
                even += 1
                
            #Odd
            else:
                odd += 1
        
        return min(even, odd)