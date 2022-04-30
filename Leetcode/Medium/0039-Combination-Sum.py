class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        # Time: O(2^n)
        # Space: O(2^n)
        
        # Brute force and stop when running sum exceeds target
        def dfs(runningSum, path, nums):
            if runningSum == target:
                output.append(path)
            
            # Two decisions: either use the number and include it, or skip it altogether
            if runningSum < target and len(nums):
                dfs(runningSum + nums[0], path + [nums[0]], nums[:]) # Include
                dfs(runningSum, path, nums[1:]) # Not include
                    
        output = []
        dfs(0, [], candidates)
        return output