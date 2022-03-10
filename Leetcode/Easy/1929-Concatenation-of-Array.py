class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        #Time: O(n)
        #Space: O(n)
        
        output = [None for _ in range(len(nums) * 2)]
        
        for idx in range(len(nums)):
            output[idx] = nums[idx]
            output[idx + len(nums)] = nums[idx]
        
        return output