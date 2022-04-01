class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        # Time: O(n)
        # Space: O(n)
        
        output = [None for _ in range(len(nums))]
        left, right = 0, len(nums) // 2
        ptr = 0
        
        for _ in range(n):
            output[ptr] = nums[left]
            output[ptr + 1] = nums[right]
            
            left += 1; right += 1
            ptr += 2
        
        return output