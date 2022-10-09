class Solution:
    def twoSumLessThanK(self, nums: List[int], k: int) -> int:
        # Time: O(nlogn)
        # Space: O(1)
        
        nums.sort()
        
        l, r = 0, len(nums) - 1
        max_sum = -1
        
        while l < r:
            cur_sum = nums[l] + nums[r]
            
            if cur_sum >= k:
                r -= 1
            else:
                max_sum = max(max_sum, cur_sum)
                l += 1
                
        return max_sum
        