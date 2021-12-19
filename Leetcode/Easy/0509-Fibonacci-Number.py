class Solution:
    def fib(self, n: int) -> int:
        #Time: O(n)
        #Space: O(n)
        
        if n < 2: return n
        
        memoize = [float(inf)] * (n + 1)
        memoize[0], memoize[1] = 0, 1
        
        for idx in range(2, n + 1):
            memoize[idx] = memoize[idx - 1] + memoize[idx - 2]

        return memoize[-1]