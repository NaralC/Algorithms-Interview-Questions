class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #Time: O(n)
        #Space: O(1)
        
        #Only buy today and sell tomorrow if tomorrow's price is higher than today's
        #In other words, only add up positive interval differences to the result
        
        profit = 0
        
        for idx in range(len(prices) - 1):
            today, tmr = prices[idx], prices[idx + 1]
            
            if tmr - today > 0:
                profit += tmr - today
                
        return profit