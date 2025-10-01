class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Time: O(n)
        # Space: O(1)
        output = 0
        buy, sell = 0, 1

        while sell < len(prices):
            # Found a lower point to buy, move buy
            if prices[sell] < prices[buy]: buy = sell

            # Always scan for better profit
            output = max(output, prices[sell] - prices[buy]) 
            
            sell += 1
        
        return output
