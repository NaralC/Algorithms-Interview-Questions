class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        #Time: O(n) looping over the input twice
        #Space: O(n) since we're using a monotonic stack
        #The idea is the same with "Daily Temperatures", but here we loop over the input array twice to see if there's really a greater element to the left
        
        output = [-1] * len(nums)
        stack = [] #[val, idx]
        
        for idx in range(len(nums) * 2):
            idx %= len(nums)
            curNum = nums[idx]
            
            while len(stack) and curNum > stack[-1][0]:
                info = stack.pop()[-1]
                output[info] = curNum
            
            stack.append([curNum, idx])
        
        return output