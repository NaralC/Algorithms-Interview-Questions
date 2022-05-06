class Solution:
    def myPow(self, num: float, expo: int) -> float:
        # Time: O(logn)
        # Space: O(logn)
        
        def helper(num, expo):
            # Edge cases
            if num == 0: return 0 # 0's can't be raised
            if expo == 0: return 1 # Numbers raised to 0 evaluate to 1
            
            output = helper(num, expo // 2)
            output *= output
            
            # Only odd exponents require another multiplication with the base num
            return output if expo % 2 == 0 else output * num
        
        # Only odd exponents require flipping the output before shipping
        output = helper(num, abs(expo))
        return output if expo >= 0 else 1 / output