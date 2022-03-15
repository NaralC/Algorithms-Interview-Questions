class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        #Time: O(n)
        #Space: O(n)
        
        output = []
        prefix = 0
        
        for num in nums:
            prefix += num
            output.append(prefix)
        
        return output