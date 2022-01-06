class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #Time: O(n)
        #Space: O(1)
        
        buy, sell = 0, 1
        output = 0
        
        while sell < len(prices):
            #1) Better profit
            if (profit := prices[sell] - prices[buy]) > output:
                output = profit
            
            #2) Lower buying price
            if prices[buy] > prices[sell]:
                buy = sell
            
            sell += 1
        
        return output