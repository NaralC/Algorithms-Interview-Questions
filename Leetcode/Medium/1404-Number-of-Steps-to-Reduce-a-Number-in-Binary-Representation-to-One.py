class Solution:
    def numSteps(self, s: str) -> int:
        # Time: O(n)
        # Space: O(1)
        
        l, zero_count = 0, 0
        
        # The leftmost number is always '1', no leading '0's
        for r in range(1, len(s)):
            if s[r] == '1':
                zero_count += r - l - 1 # Add up with the distance between left and righ ptr
                l = r
        
        # Even cases like '10000'
        if l == 0:
            return len(s) - 1 
        
        # Odd cases, mixture of '0's and '1's
        return zero_count + 1 + len(s)

            