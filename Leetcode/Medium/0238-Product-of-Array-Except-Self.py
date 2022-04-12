class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Time: O(n)
        # Space: O(1)
        
        # Assign the current running product to the output off by 1 position depending on the side of approach
        output = [1 for _ in range(len(nums))]
        
        # Compute running product from the left
        prod = 1
        
        for idx in range(len(nums) - 1):
            prod *= nums[idx]
            output[idx + 1] *= prod
        
        # Compute running product from the right
        prod = 1
        
        for idx in range(len(nums) - 1, 0, -1):
            prod *= nums[idx]
            output[idx - 1] *= prod
        
        return output