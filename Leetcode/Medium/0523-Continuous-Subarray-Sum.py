class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        # Time: O(n)
        # Space: O(n)
        # If we get the same remainder again, then we've encountered some sum which is a multiple of K
        
        remainder = {0 : -1} # {Remainder : End idx}
        total = 0
        
        for idx, num in enumerate(nums):
            total += num
            r = total % k
        
            if r not in remainder:
                remainder[r] = idx
            elif idx - remainder[r] > 1:
                return True
        
        return False