class Solution:
    def arrangeCoins(self, n: int) -> int:
        #Time: O(logn)
        #Space: O(1)
        
        left, right = 0, n 
        
        while left <= right:
            row = (left + right) // 2
            
            #At row number {row}, we do not need more than this number of coins to construct a row
            max_coins = (row * (row + 1)) // 2
            
            if max_coins == n:
                return row
            elif max_coins < n:
                left = row + 1
            elif max_coins > n:
                right = row - 1
        
        #Since the last row could be incomplete, return right for the -1 effect
        return right