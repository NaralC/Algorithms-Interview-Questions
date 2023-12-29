class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Time: O(n)
        # Space: O(1)

        buy, sell = 0, 1 # Indexes
        best = 0

        while sell < len(prices):
            # Finds better best price
            if (profit := prices[sell] - prices[buy]) > best:
                best = profit

            # Finds cheaper buying price
            elif (todaysPrice := prices[sell]) < prices[buy]:
                buy = sell

            sell += 1

        return best
        