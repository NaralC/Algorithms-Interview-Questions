class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        #Time: O(n * m) where n = amount, m = len(coins)
        #Space: O(n)
        
        memoize = [float(inf)] * (amount + 1) #We can't fill it with None due to the min() below
        memoize[0] = 0 #Making a change of 0 requires 0 coin
        
        for target in range(1, amount + 1):
            for coin in coins:
                #Only try out with coins fit current change target
                if coin > target: continue
                
                #Track the minimum amount of coin usage when trying different coins
                memoize[target] = min(memoize[target], 1 + memoize[target - coin])
        
        #Return -1 if the last element (a.k.a target amount) hasn't been touched
        return memoize[-1] if memoize[-1] != float(inf) else -1