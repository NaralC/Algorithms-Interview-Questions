class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        #Time: O(n)
        #Space: O(n)
        
        output = [None for _ in range(len(nums))]
        
        for idx, num in enumerate(nums):
            output[idx] = nums[num]
        
        return output