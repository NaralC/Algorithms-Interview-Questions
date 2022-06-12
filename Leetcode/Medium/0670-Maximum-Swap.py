class Solution:
    def maximumSwap(self, num: int) -> int:
        # Time: O(nlogn)
        # Space: O(n)
        
        # No need to swap if num's already in descending order
        num = list(str(num))
        
        if sorted(num, reverse = True) == num:
            return int(''.join(num))
        
        # Loop backwards, keep track of the largest number, and swap it with a smaller number to its left
        max_num, max_idx = -1, -1
        left, right = None, None # Is used for swapping later
        
        for idx in reversed(range(len(num))):
            # Bigger number detected
            if num[idx] > str(max_num):
                max_num = num[idx]
                max_idx = idx
            
            # Smaller number to the biggest detected
            elif num[idx] < str(max_num):
                left = idx
                right = max_idx
                
        num[left], num[right] = num[right], num[left]
        
        return int(''.join(num))
