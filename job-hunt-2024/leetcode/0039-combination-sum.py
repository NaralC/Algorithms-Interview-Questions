class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        # Time: O(2^n)
        # Space: O(2^n)
        
        output = []

        def dfs(nums, runningSum, path):
            if runningSum >= target: 
                output.append(path)
                return
            if runningSum > target: 
                return
            
            if len(nums):
                # Use and keep the number. This covers both cases of using a number n times/once
                dfs(nums[:], runningSum + nums[0], path + [nums[0]]) 
                # Skip and discard the number
                dfs(nums[1:], runningSum, path)

        dfs(candidates, 0, [])
        return list(output)